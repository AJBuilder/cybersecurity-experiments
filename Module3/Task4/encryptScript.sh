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
single1=`echo "$used1 / 10" | bc -l`
echo "That's an average of $single1 msec to encrypt once"

echo ""

echo "####################Start####################"
echo "Do RSA dec 10,000 times"
echo "command line:"
echo "openssl pkeyutl -decrypt -passin pass:password -pubin -inkey private.key -in m_enc.txt -out m_dec.txt"
start2=`date '+%s'`    
for i in $(seq 0 10000)
do
openssl pkeyutl -decrypt -passin pass:password -pubin -inkey private.key -in m_enc.txt -out m_dec.txt 1> /dev/null 2>&1
done
finish2=`date '+%s'`
used2=`echo "$finish2-$start2" | bc`
echo "Total time: $used2 sec"
single2=`echo "$used2 / 10" | bc -l`
echo "That's an average of $single2 msec to decrypt once"


echo ""

echo "####################Start####################"
echo "Do AES-128-ECB encryption 10,000 times"
echo "command line:"
echo "openssl enc -aes-128-ecb -K 000102030405060708090A0B0C0D0E0F -in m.txt -out m_aes_enc.txt"
start3=`date '+%s'`    
for i in $(seq 0 10000)
do
openssl enc -aes-128-ecb -K 000102030405060708090A0B0C0D0E0F -in m.txt -out m_aes_enc.txt
done
finish3=`date '+%s'`
used3=`echo "$finish3-$start3" | bc`
echo "Total time: $used3 sec"
single3=`echo "$used3 / 10" | bc -l`
echo "That's an average of $single3 msec to encrypt once"

