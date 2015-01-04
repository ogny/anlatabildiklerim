=============================
Advanced Bash Scripting Guide
=============================

:date: 2015-01-02

* **motto**: The only way to really learn scripting is to write scripts.

Ne ogrendim? 
============
  
Syntax'a dair; 
--------------

- COMMENT satiri devam ettiginde basina + koy
- Degisken adini kucuk harf tanimladiysan $ ile cagiriken kucuk harle, veya
  tersi sekilde cagir.
- Bulundugun dizindeki betigi cagiriyorken basa ./ ekle, neden?
  for security reasons, the current directory (./) is not by default included
  in a user's $PATH. It is therefore necessary to explicitly invoke the script
  in the current directory with a ./scriptname

Lazim olabilecek Kod parcalari
------------------------------

- The following script prolog tests whether the script has been invoked with
  the correct number of parameters. 

.. code:: sh

    E_WRONG_ARGS=85
    script_parameters="-a -h -m -z"
    #                  -a = all, -h = help, etc.
    
    if [ $# -ne $Number_of_expected_args ]
    then
      echo "Usage: `basename $0` $script_parameters"
      # `basename $0` is the script's filename.
      exit $E_WRONG_ARGS
    fi


Special Characters
------------------

- Terminator in a case option 

.. code:: sh

   ;;

- Terminators in a case option (version 4+ of Bash).

.. code:: sh

   ;;&, ;&

- The *comma* operator can also concatenate strings

.. code:: sh

    for file in /{,usr/}bin/*calc
    #             ^    Find all executable files ending in "calc"
    #+                 in /bin and /usr/bin directories.
    do
            if [ -x "$file" ]
            then
              echo $file
            fi
    done

**Not**: comma operatoru degisiklik yapilacak sistem
dosyasinin yedegi alinirken gunluk olarak kullaniliyor 


.. code:: sh

    cp dosya{,.original} 

- Lowercase conversion in parameter substitution 

.. code:: sh

   ,, ,

- command substitution. The `command` construct makes available the output of
  command for assignment to a variable. This is also known as backquotes or
  backticks.

.. code:: sh

   `

- null command [colon]. This is the shell equivalent of a "NOP" (no op, a
  do-nothing operation). It may be considered a synonym for the shell builtin
  true. The ":" command is itself a Bash builtin, and its exit status is true

.. code:: sh

  (0).:echo $?   # 0

- Variable expansion / substring replacement.In com bination with the >
  redirection operator, truncates a file to zero length, without changing its
  permissions. If the file did not previously exist, creates it.

.. code:: sh

    : > data.xxx   # File "data.xxx" now empty.	      
    
    # Same effect as   cat /dev/null >data.xxx
    # However, this does not fork a new process, since ":" is a builtin.




- The "?" character serves as a single-character "wild card" for
  filename expansion in globbing, as well as representing one character in an
  extended regular expression.

