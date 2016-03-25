#include <iostream>
#include <WinSock2.h>
#include <event2/event.h>
#include <event2/buffer.h>
#include <event2/bufferevent.h>
using namespace std;

//初始化Socket，Windows程序使用Socket前必须调用
void init()
{
	WORD sockVersion = MAKEWORD(2,2);//使用第2版协议
	WSADATA wsaData;
	if(WSAStartup(sockVersion, &wsaData)!=0)
	{
		cout<<"init error"<<endl;
		return ;
	}
}

//收到数据的回调函数
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

//创建数据读取线程
DWORD WINAPI readThreadFunction(LPVOID lpParameter)
{
	//创建event_base
	struct event_base *base;
	base = event_base_new();
	if(!base)
	{
		cout<<"init event_base error"<<endl;
		return -1;
	}

	//创建并添加event，EV_PERSIST表示事件不会被删除
	SOCKET *client = (SOCKET *)lpParameter;
	
	struct bufferevent *bev;
	bev = bufferevent_socket_new(base,*client,BEV_OPT_CLOSE_ON_FREE);
	bufferevent_setcb(bev,on_read,NULL,NULL,NULL);
	bufferevent_enable(bev,EV_READ);

	//开启消息循环
	event_base_dispatch(base);
	return 0;
}


void runLibeventClient()
{
	init();

	//创建一个Socket并连接
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

	//将listener设置成为阻塞
	evutil_make_socket_nonblocking(client);
	
	//创建读取线程,将client作为参数传入
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