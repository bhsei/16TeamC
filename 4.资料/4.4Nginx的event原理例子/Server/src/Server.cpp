#include <iostream>
#include <WinSock2.h>
#include <event2/event.h>
#include <event2/buffer.h>
#include <event2/bufferevent.h>

using namespace std;

//��ʼ��Socket��Windows����ʹ��Socketǰ�������
void init()
{
	WORD sockVersion = MAKEWORD(2,2);//ʹ�õ�2��Э��
	WSADATA wsaData;
	if(WSAStartup(sockVersion, &wsaData)!=0)
	{
		cout<<"init error"<<endl;
		return ;
	}
}

//��ȡ���ݻص�����
void on_read(struct bufferevent *bev, void *ctx)
{
	struct evbuffer *input = bufferevent_get_input(bev);
	struct evbuffer *output = bufferevent_get_output(bev);
	char *line;
	size_t cnt;
	while(line = evbuffer_readln(input,&cnt,EVBUFFER_EOL_ANY))
	{
		cout<<"receive:"<<line<<endl;

		//д������
		evbuffer_add(output,"hello ",6);
		evbuffer_add(output,line,cnt);
		evbuffer_add(output,"\n",1);
		free(line);
	}
}

//�ͻ������ӻص�����
void do_accept(evutil_socket_t listener, short event, void *arg)
{
	struct event_base *base = (event_base*)arg;

	//�봫ͳ����һ������������
	SOCKET client;
	sockaddr_in clientAddr;
	int clientAddrLen = sizeof(clientAddr);
	client = accept(listener,(SOCKADDR*)&clientAddr,&clientAddrLen);
	if(client < 0)
	{
		cout<<"accept error"<<endl;
	}
	else//���ӳɹ���ע���ȡ�ص�����on_read
	{
		cout<<"connected"<<endl;
		struct bufferevent *bev;
		bev = bufferevent_socket_new(base,client,BEV_OPT_CLOSE_ON_FREE);
		evutil_make_socket_nonblocking(client);
		bufferevent_setcb(bev,on_read,NULL,NULL,NULL);
		bufferevent_enable(bev,EV_READ);
	}
}

void runLibeventServer()
{
	//����event_base
	struct event_base *base;
	base = event_base_new();
	if(!base)
	{
		cout<<"init event_base error";
		return;
	}

	//����һ��Socket
	SOCKET listener = socket(AF_INET,SOCK_STREAM,IPPROTO_TCP);
	if(listener == INVALID_SOCKET)
	{
		cout<<"socket error"<<endl;
		return ;
	}

	//�����ַ��
	sockaddr_in sin;
	sin.sin_family = AF_INET;
	sin.sin_port = htons(12345);
	sin.sin_addr.S_un.S_addr = INADDR_ANY;
	if(bind(listener,(LPSOCKADDR)&sin,sizeof(sin)) == SOCKET_ERROR)
	{
		cout<<"bind error"<<endl;
		return;
	}

	//��listener���ó�Ϊ������
	evutil_make_socket_nonblocking(listener);

	//��ʼ����
	if(listen(listener,5) == SOCKET_ERROR)
	{
		cout<<"listen error"<<endl;
		return;
	}
	
	//���������event��EV_PERSIST��ʾ�¼����ᱻɾ��
	struct event *listener_event = event_new(base,listener,EV_READ|EV_PERSIST,do_accept,(void*)base);
	event_add(listener_event,NULL);
	
	//������Ϣѭ��
	event_base_dispatch(base);
}

int main()
{
	init();
	cout<<"Server started"<<endl;
	runLibeventServer();
	return 0;
}

