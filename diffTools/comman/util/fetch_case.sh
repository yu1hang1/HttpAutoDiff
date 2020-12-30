#!/bin/bash
#./fetch_case.sh -d 2020-03-16 -a manage -p ./data -s SnapshotRemote  -m buildDraftSnap

Usage() {
  #  echo "$* $@"
  echo "USAGE: ./fetch_case.sh -d <yyyy-mm-dd>  -a <app_code> -s <service_name> -m <method_name>"
  echo "  -d: monday every week, eg. -d 20190311"
  echo "  -a: app code name, default is manage"
  echo "  -s: service name, default is SnapshotRemote"
  echo "  -m: method name, default is buildDraftSnap"
  exit 1
}

while getopts "d:p:a:s:m:" OPTION; do
  case $OPTION in
  d)
    date=$OPTARG
    ;;
  a)
    app_code=$OPTARG
    ;;
  s)
    service_name=$OPTARG
    ;;
  m)
    method_name=$OPTARG
    ;;
  ?)
    Usage
    ;;
  esac
done
if [ ! $date ]; then
  Usage
fi

if [ ! $app_code ]; then
  Usage
fi
if [ ! $service_name ]; then
  Usage
fi
if [ ! $method_name ]; then
  Usage
fi

echo "parameter values:"
echo "data=$date"
echo "app_code=$app_code"
echo "service_name=$service_name"
echo "method_name=$method_name"

declare svrlist=()

#根据app_code获取服务器列表
case $app_code in
manage)
    svrlist=(display-manage1.idss.w.bj1 display-manage2.idss.w.bj1)
    tomcatName="chenlie.wormpex.com";;
user)
  svrlist=(display-user1.idss.w.bj1)
  tomcatName="display-user.opc.com";;
cristina)
  svrlist=(display-cristina2.idss.w.bj1)
  tomcatName="chenlie-cristina.wormpex.com";;
monitor)
  svrlist=(display-monitor2.idss.w.bj1)
  tomcatName="display-monitor.wormpex.com";;
core)
  svrlist=(snap-core3.app.display.bj1)
  tomcatName="display_app_snap_core";;
  *)
    echo "sorry ,haven't the app_code"
    exit 1
  esac


doSyncSingleSummaryCountMethod() {
  echo /home/w/www/$2/logs/dubbo-access-provider.$date*
  echo "zcat /home/w/www/$2/logs/dubbo-access-provider.$date* | grep $service_name|grep $method_name | head -1 | awk -F'DONE' '{print \$2}' | tr -d ' '>~/$method_name.$date"
  ssh $1 "zcat /home/w/www/$2/logs/dubbo-access-provider.$date* | grep $service_name|grep $method_name | head -1 | awk -F'DONE' '{print \$2}' | tr -d ' '>~/$method_name.$date"
  scp $1:~/$method_name.$date ~/case_root/$method_name.$date
  ssh $1 "rm -r ~/*"

}

for svr in ${svrlist[@]};
do
  echo $svr
  echo $tomcatName
  doSyncSingleSummaryCountMethod $svr $tomcatName

done

