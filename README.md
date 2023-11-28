# M3U

## 指令处理

sed -i '/韩国金先生/s/group-title="未分类"/group-title="韩国金先生"/g' 44095.m3u
sed -i '/天美赵公子/s/group-title="[^"]*"/group-title="天美传媒"/g' 44095.m3u

sed -i '/蜜桃传媒/s/group-title="[^"]*"/group-title="蜜桃传媒"/g' 44095.m3u



sed -i '/乌鸦传媒/s/group-title="[^"]*"/group-title="乌鸦传媒"/g' madou.m3u

sed -i '/精东影业/s/group-title="[^"]*"/group-title="精东影业"/g' madou.m3u

sed -i '/星空传媒/s/group-title="[^"]*"/group-title="星空传媒"/g' madou.m3u


sed -i '/果冻传媒/s/group-title="[^"]*"/group-title="果冻传媒"/g' madou.m3u

sed -i '/group-title/s/group-title="[^"]*"/group-title="玩偶姐姐"/g' hkd.m3u

group-title="SA国际",

tvg-id="SA国际" group-title="国产传媒",

group-title="旗袍", 

tvg-id="旗袍" group-title="xxx",

grep group-title

grep -o 'group-title="[^"]*"' hushi.m3u | sed 's/group-title="//;s/"$//' | sort -u


group-title="七度空间",
group-title="国产传媒", 七度空间 



sed -i 's/\(TMY\)\([0-9]\{4\}\)/ tvg-id="\1\2",/' madou.m3u
sed -i 's/\(TMY\)\([0-9]\{3\}\)/ tvg-id="\1\2",/' madou.m3u


sed -i 's/\(TMW-\)\([0-9]\{3\}\)/ tvg-id="\1\2",/' madou.m3u

sed -i 's/\(TWA\)\([0-9]\{4\}\)/ tvg-id="\1\2",/' madou.m3u

sed -i 's/JD[A-Za-z0-9]*/ tvg-id="\1\2",/' madou.m3u

sed -i 's/\(QQOG-\)\([0-9]\{3\}\)/ tvg-id="\1\2",/' madou.m3u
sed -i 's/\(QQCM\)\([0-9]\{3\}\)/ tvg-id="\1\2",/' madou.m3u

sed -i 's/\(SJ\)\([0-9]\{3\}\)/ tvg-id="\1\2",/' madou.m3u

sed -i 's/\(π\)\([0-9]\{3\}\)\ / tvg-id="\1\2",/' madou.m3u
sed -i 's/\(π\)\([0-9]\{2\}\)\ / tvg-id="\1\2",/' madou.m3u
sed -i 's/\(π\)\([0-9]\{1\}\)\ / tvg-id="\1\2",/' madou.m3u




