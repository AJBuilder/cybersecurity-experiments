#!/bin/sh
echo "####################Start####################"
echo "Do RSA enc 10,000 times"
echo "command line:"
echo "openssl pkeyutl -encrypt -pubin -inkey public.key -in m.txt -out m_enc.txt"
start1=`date '+%s'`
for i in $(seq 0 10000)
do
openssl pkeyutl -encrypt -pubin -inkey public.key -in m.txt -out m_enc.txt 1> /dev/null 2>&1
done
finish1=`date '+%s'`
used1=`echo "$finish1-$start1" | bc`
echo "Total time: $used1 sec"
single1=`echo "$used1 / 10000" | bc`
echo "That's and average of $single1 sec to encrypt once"

openssl pkeyutl -decrypt -inkey private.key -in m_enc.txt -out m_dec.txt

echo "####################Start####################"
echo "Do RSA dec 10,000 times"
echo "command line:"
echo "openssl rsautl -encrypt -pubin -inkey public.pem -in m.txt -out m_enc.txt"
start1=`date '+%s'`    
for i in $(seq 0 10000)
do
openssl pkeyutl -decrypt -passin pass:password -pubin -inkey public.key -in m_enc.txt -out m_dec.txt 1> /dev/null 2>&1
done
finish1=`date '+%s'`
used1=`echo "$finish1-$start1" | bc`
echo "Total time: $used1 sec"
single1=`echo "$used1 / 10000" | bc`
echo "That's and average of $single1 sec to encrypt once"
