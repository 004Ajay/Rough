echo "Enter a limit number: "
read num
echo "Natural numbers from 1 to" $num ":"
for((i = 1; i <= num; i++))
do
echo $i
done