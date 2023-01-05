#!/usr/bin/env python
# coding: utf-8

# Technicians in a pathology lab analyze digitized images of slides. Objects on a slide are selected for
# analysis by a mouse click on the object. The perimeter of the boundary of an object is one useful
# measure. Your task is to determine this perimeter for selected objects.
# The digitized slides will be represented by a rectangular grid of periods, '.', indicating empty space,
# and the capital letter 'X', indicating part of an object. 

# In[5]:


import pandas as pd
import numpy as np


# In[ ]:


using namespace std;
const int maxn=222;
char mp[maxn][maxn];
int book[maxn][maxn];
int n,m,xx,yy;


# In[ ]:


int dire[][2]={-1,0,1,0,0,-1,0,1,-1,-1,-1,1,1,-1,1,1,1};


# In[ ]:


int ans;


# In[ ]:


def dfs (int x, int y)
{
    for(int x,int y)
    {
        int nx =x+dire[i][0];
        int ny=y+dire[i][1];
        if(nx<1||nx>n||ny<1||ny>m||mp[nx][ny]=='.')ans++;
        
    }
    for (int i=0;i<8;i++)
    {
        int nx=x+dire[i][0];
        int ny=y+dire[i][1];
        if (nx<1||nx>n||ny<1||ny>m)continue;
        if (!book[nx][ny]&&mp[nx][ny]=='X'){
            book[nx][ny]=1;
            dfs(nx,ny);
        }
        
    }
}
 int  main()
{
    while(c>>n>>m>>xx>>yy,n+m+xx+yy)
    {
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=m;j++)cin>>mp[i][j];
        }
        ans=0;
        memset(book,0,sizeof(book));
        if(mp[xx][yy]=='.'){
           print<<0<<end1;
            continue;
            
        }
        book[xx][yy]=1;
        dfs(xx,yy);
        print<<ans<<end1;
    }
    returns0;
}

