Title: 理解iOS code signing
Date: 2013-09-02 9:17
Category: iOS
Tags: iOS,cocoa,deploy 
Slug: understand-iOS-code-signing
Author: Tony Zhou

用iOS模拟器调试App是一件容易的事情，可是当你要放到iPhone或者iPad时运行应用时，就需要额外做很多事情：

* 申请一个iOS开发者帐户（iOS developer program）
* 生成一个development／Distribution Certificate
* 在开发者帐户中添加AppID， 添加devices
* 生成一个provision文件
* 在Xcode中，对project的code signing identity作正确的配置

##iOS developer Program

iOS developer program分成三种：iOS developer （Standard） program（以下简称iDP）、iOS developer Enterprise Program（以下简称iDEP）和iOS developer University Program。 IDP用于以个人或者公司的身份在Appstore上开发应用；iDEP用于in-house App的开发， in-house的App不能上Appstore，只能在组织内进行分发；iOS developer University Program用于高等院校将iOS开发引入课程。注意，不要把以公司身份申请的iDP和iDEP混淆。 iDP可以用个人身份申请，也可以以公司身份申请，两者在申请时提供的资料不一样，个人的iDP不能添加子帐户，而公司的IDP可以添加子帐户，但是它们都可以把应用发布到Appstore上面，费用都是99刀，可以ad hoc部署设备都只有100台。 而iDEP可以部署的设备是无限的，唯独不能发布应用到Appstore中，一年的费用是299刀。 

##Development certificate 和 distribute certificate

Certificate就是一个证书，关于证书有何用处，阮一峰有一篇[blog](http://www.ruanyifeng.com/blog/2011/08/what_is_a_digital_signature.html)，非常浅显易懂。简要的说，证书=公钥+元数据+签名。和公钥配对的私钥是保密的，私钥被存放在钥匙串应用程序中（可导出为.p12文件，迁移到其他机器上）；公钥要和元数据一起，发往证书颁发机构（CA），由CA签名之后，生存一份有效的证书，证书是公开的，在provisioning profile文件中一般会有证书的副本。

生成证书的具体过程是这样的： 首先我们用钥匙串应用生成一个证书请求文件（Certificate request）。在生成证书请求文件的过程中，我们就已经产生了一对密钥，私钥放在本地，公钥+一部分元数据被放到了证书请求文件中。证书颁发机构接收到证书请求文件之后，用它自己的私钥对其进行签名，返回一个有效证书。 我们要把这个证书再添加到钥匙串应用中，使它和之前的私钥进行配对。

为什么真机测试需要用到证书和密钥？ 因为iOS只允许来源可信的应用程序在其操作系统上运行。 每个App需要有一个苹果颁发的证书，确保它不是来源不明的应用；在安装的过程中，iOS还要验证App的可执行文件以及其他资源的数字签名，确保它们没有受到恶意修改。

真机测试涉及到的certificate有两种：development certificate和distribution certificate， development certificate可以建立多个副本， 而distribution certificate只能建立一个副本，所以如果要在另外一台Mac机器上共用distribution certificate，就只能在原先的机器上把密钥导出，再将其导入新机器的钥匙串应用程序中。 distribution certificate除了用于AppStore发布，还主要被用作beta测试，因为它能使用ad hoc部署的方式将应用安装到目标机器上。

##App ID和Device UDID

App ID 就是一个应用的application identifier，在developer program页面，可以建立两种App ID，一种是明确（explicit）的，比如com.example.myapp; 一种是基于通配符（wildcard）的，比如*和com.example.*，如果应用涉及到推送通知和应用内购买，则必须使用explicit的AppID。在创建provision profile时，我们还需要选择这个App ID，因此，它必须和xcode中identifier的配置一样。

Device UDID用于标识一台苹果设备，provisioning profile中必须指出这个应用要部署在哪几台设备上，这些设备是通过UDID唯一标识的。 一个开发者账户能添加的设备最多只有100台，若要在某台机器上测试刚开发的应用，必须先将这台设备的UDID添加到iDP中。

##Provisioning

Provisioning profile包含了以上谈论的各种配置信息: 证书，App ID，设备UDIDs，可以用文本编辑器打开~/Library/MobileDevice/Provisioning Profiles下的.mobileprovision文件查看具体内容。xcode在编译产生app bundle时，会将对应的mobileprovision文件拷贝到bundle中，文件名是embedded.mobileprovision， 通过diff命令比较embedded.mobileprovision和provision profiles下的mobileprovision文件可以发现，除了文件名不同，文件内容都是一样的。注意，不能自己随意的修改这个mobileprovision文件，每次添加设备后，必须从iDP网站上同步最新的provision文件，因为该文件必须经过Apple的数字签名，无法随意伪造。

##Code Sign过程

准备好上述的各种文件之后，我们要在xcode中为target制定code sign identity，code sign就是利用私钥对app bundle中的文件生成一段数字签名，并将数字签名附在bundle中，code sign有两个作用：1. 确保可执行文件的来源可靠， 2. 确保可执行文件没有遭到恶意修改。 苹果在xcode命令行工具中附带了一个命令codesign，可以用man codesign命令查看其具体用法。


附录：

* Apple document: [code signing your Apps](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/CodeSigningYourApps/CodeSigningYourApps.html)

* Apple document: [code signing guide](https://developer.apple.com/library/mac/documentation/security/conceptual/CodeSigningGuide/Introduction/Introduction.html)

* Ray Wenderlich: [iOS code signing under the hood](http://www.raywenderlich.com/2915/ios-code-signing-under-the-hood)

* wikipedia: [code signing](http://en.wikipedia.org/wiki/Code_signing)

* OS X Manpage:[codesign](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/codesign.1.html)
