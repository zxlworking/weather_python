#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-

from com_zxl_send_message.CCPRestSDK import REST


#���ʺ�
accountSid= '8a216da865e6d0370165fa85622c0ae0'

#���ʺ�Token
accountToken= '538983581e4f4a4db33c17754383c7fb'

#Ӧ��Id
appId='8a216da865e6d0370165fa85627c0ae6';

#�����ַ����ʽ���£�����Ҫдhttp://
serverIP='app.cloopen.com';

#����˿�
serverPort='8883';

#REST�汾��
softVersion='2013-12-26';

  # ����ģ�����
  # @param to �ֻ�����
  # @param datas �������� ��ʽΪ���� ���磺{'12','34'}���粻���滻���� ''
  # @param $tempId ģ��Id

def sendTemplateSMS(to,datas,tempId):


    #��ʼ��REST SDK
    rest = REST(serverIP,serverPort,softVersion)
    rest.setAccount(accountSid,accountToken)
    rest.setAppId(appId)
    
    result = rest.sendTemplateSMS(to,datas,tempId)
    for k,v in result.iteritems(): 
        
        if k=='templateSMS' :
                for k,s in v.iteritems(): 
                    print '%s:%s' % (k, s)
        else:
            print '%s:%s' % (k, v)
    
   
#sendTemplateSMS(�ֻ�����,��������,ģ��Id)