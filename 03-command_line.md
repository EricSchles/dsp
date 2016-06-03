# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

1. CTRL+C : halts the current command / kills the current program
2. CTRL+R : reverse search history
3. CTRL+U : kills backward from point to the beginning of line
4. CTRL+Y : Retrieves the last item that was killed (undo in a sense)
5. clear / CTRL + L : clears the terminal
6. chmod -options <filename> : lets you change the read, write, and execute permissions on your files
7. TAB : auto completion of file or command
8. pwd : print working directory
9. !! : repeat last command
10. touch <filename> : create or update a file

---

###Q2.  List Files in Unix

What do the following commands do:
`ls` : List files (not including hidden files)
`ls -a` : List all files, including hidden files
`ls -l` : List files in long format and includes additional details >> files permissions, number of links, owner name, owner group, file size, times of last modification, and file/directory name
`ls -lh` : Options can be chained together, so this is combing the "-l" and the "-h" (which places it in human readable format)
`ls -lah`: This combines the -l, -a, and -h options (see above definitions). Listing all files/directories (including hidden ones) in full detail in a human readable format
`ls -t` : List files and sort by time modified (most recently modified first) before sorting the operands by lexicographical order.
`ls -Glp` : Once again this is a chaining of commands. "-G" enables colorized output, "-l" lists the files in long format, and "-p" will include a slash (`/') after each filename if that file is a directory

---

###Q3.  More List Files in Unix

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

1. -1 : Displays each entry on a line.
2. -R : Displays subdirectories as well.
3. -d : Displays only directories.
4. -r : Displays files in reverse order.
5. -q : Displays all non-printing characters as ?

---

###Q4.  Xargs

What does `xargs` do? Give an example of how to use it.

'xargs' enables you to read arguments from the "standard input" and execute them. In the example below, there are two commands that are chained together. The first half looks for files that have names that meet have the ".md" extension. Afterwards, the grep command (global regular expressions print) searches within each of the applicable files for the word "code", based on arguments provided initially in the first half.

Example: find . -name "*.md" | xargs grep "code"


