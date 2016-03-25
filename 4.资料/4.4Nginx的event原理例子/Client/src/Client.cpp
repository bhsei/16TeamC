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

//�յ����ݵĻص�����
void on_read(struct bufferevent *bev, void *ctx)
{
	struct evbuffer *input = bufferevent_get_input(bev);
	struct evbuffer *output = bufferevent_get_output(bev);
	char *line;
	size_t cnt;
	while(line = evbuffer_readln(input,&cnt,EVBUFFER_EOL_ANY))
	{
		cout<<"receive:"<<line<<endl;
	}
}

//�������ݶ�ȡ�߳�
DWORD WINAPI readThreadFunction(LPVOID lpParameter)
{
	//����event_base
	struct event_base *base;
	base = event_base_new();
	if(!base)
	{
		cout<<"init event_base error"<<endl;
		return -1;
	}

	//���������event��EV_PERSIST��ʾ�¼����ᱻɾ��
	SOCKET *client = (SOCKET *)lpParameter;
	
	struct bufferevent *bev;
	bev = bufferevent_socket_new(base,*client,BEV_OPT_CLOSE_ON_FREE);
	bufferevent_setcb(bev,on_read,NULL,NULL,NULL);
	bufferevent_enable(bev,EV_READ);

	//������Ϣѭ��
	event_base_dispatch(base);
	return 0;
}


void runLibeventClient()
{
	init();

	//����һ��Socket������
	SOCKET client = socket(AF_INET,SOCK_STREAM,IPPROTO_TCP);
	if(client == INVALID_SOCKET)
	{
		cout<<"socket error"<<endl;
		return ;
	}

	sockaddr_in sin;
	sin.sin_family = AF_INET;
	sin.sin_port = htons(12345);
	sin.sin_addr.S_un.S_addr = inet_addr("127.0.0.1");

	cout<<"connecting"<<endl;
	if(connect(client,(LPSOCKADDR)&sin,sizeof(sin)) == SOCKET_ERROR)
	{
		cout<<"connect error"<<endl;
		return;
	}
	else
	{
		cout<<"connected"<<endl;
	}

	//��listener���ó�Ϊ����
	evutil_make_socket_nonblocking(client);
	
	//������ȡ�߳�,��client��Ϊ��������
	HANDLE hThread_read = CreateThread(NULL,0,readThreadFunction,&client,0,NULL);
	CloseHandle(hThread_read);

	cout<<"input text..."<<endl;
	while(true)
	{
		char data[255]={0};
		cin>>data;
		int len = strlen(data);
		data[len]='\n';
		int n_write = send(client,data,strlen(data),0);
		if(n_write<=0)
		{
			cout<<"send error"<<endl;
			return ;
		}
	}
}

int main()
{	
	cout<<"Client started"<<endl;
	runLibeventClient();
	return 0;
}