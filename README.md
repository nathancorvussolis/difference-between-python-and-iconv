# difference-between-python-and-iconv

## Environment

* cygwin 2.6.0 (0.304/5/3)

## Version

* Python 3.4.5
* libiconv 1.14

## Link

Python

https://www.python.org/

libiconv

http://www.gnu.org/software/libiconv/

EUC-JIS-2004 Text File

http://x0213.org/codetable/euc-jis-2004-with-char.txt

Shift_JIS-2004 Text File

http://x0213.org/codetable/sjis-0213-2004-with-char.txt

---

## EUC-JIS-2004

    $ python3 pconv.py euc_jis_2004 euc-jis-2004-with-char.txt utf_8 euc-jis-2004-python.txt

    $ iconv -f EUC-JIS-2004 -t UTF-8  euc-jis-2004-with-char.txt > euc-jis-2004-iconv.txt

    $ diff euc-jis-2004-python.txt euc-jis-2004-iconv.txt > diff-euc-jis-2004.txt

## Shift_JIS-2004

    $ python3 pconv.py shift_jis_2004 sjis-0213-2004-with-char.txt utf_8 sjis-0213-2004-python.txt

    $ iconv -f Shift_JIS-2004 -t UTF-8  sjis-0213-2004-with-char.txt > sjis-0213-2004-iconv.txt

    $ diff sjis-0213-2004-python.txt sjis-0213-2004-iconv.txt > diff-sjis-0213-2004.txt
