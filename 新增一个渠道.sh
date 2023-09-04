#!/bin/bash
echo "start------------>>>>>"
CURDIR=$(cd "$(dirname "$0")";pwd)
echo ${CURDIR}
cd ${CURDIR}
# 复制2001渠道文件到新增的渠道
read -p "输入一个新的渠道(比如2005):" NEW_CHANENEl
echo 新增的渠道=channel_${NEW_CHANENEl}
mkdir channel_${NEW_CHANENEl}
cd channel_${NEW_CHANENEl}
mkdir "base"
mkdir "gameList"

echo "开始复制base 下 version 和 version.txt文件"
cp -r ${CURDIR}"/channel_2001/base/version" ${CURDIR}"/channel_${NEW_CHANENEl}/base/"
cp ${CURDIR}"/channel_2001/base/version.txt" ${CURDIR}"/channel_${NEW_CHANENEl}/base/"

echo "开始复制gameList 下 version 和 version.txt文件"
cd ${CURDIR}/channel_${NEW_CHANENEl}/gameList

gameName=(crash dragon sevenupdown ab fishprawncrab slot slotpart)
num=${#gameName[@]} 
for((i=0;i<num;i++));  
do   
echo ${gameName[i]}
mkdir ${gameName[i]}
cp -r ${CURDIR}/channel_2001/gameList/${gameName[i]}/version ${CURDIR}/channel_${NEW_CHANENEl}/gameList/${gameName[i]}
cp ${CURDIR}/channel_2001/gameList/${gameName[i]}/version.txt ${CURDIR}/channel_${NEW_CHANENEl}/gameList/${gameName[i]}/
done 

cd ${CURDIR}
python -u newChannel.py --channel ${NEW_CHANENEl}

echo "end------------>>>>>"