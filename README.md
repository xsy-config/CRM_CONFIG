# CRM_CONFIG


## installion

```shell
curl https://raw.githubusercontent.com/xsy-config/CRM_CONFIG/master/install| python
```


## useage
``` shell
$ cd  {path2project}
$ xsy       
```


## crm  命令配置信息

* 修改规则
```js
[
    ["node_modules/react-native/Libraries/NativeAnimation/RCTNativeAnimatedNodesManager.h", "#import <RCTAnimation/RCTValueAnimatedNode.h>", "#import <RCTValueAnimatedNode.h>"],
    ["node_modules/react-native-fs/package.json", "\"version\": \"v", "\"version\": \""],
    ["文件路径","需要被替换的字符串","替换后的字符串"]
]
```

## package.json 

根据最新版package.json 修改即可
