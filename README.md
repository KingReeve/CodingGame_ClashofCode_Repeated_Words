# CodingGame Clash Submission
I submitted a problem to codingame, but it might need to be made simpler, so I want to record the original here. Making it simpler kind of defeats the puzzle, I think, but maybe it is too difficult for a clash.



Goal

When proofreading, some people have a hard time time seeing repeats, especially if they're broken up onto different lines. The brain just ignores them.

Print all of the repeated words found in a string, one on each line, to help find such words when editing text.
If there are multiple matching words in a row, print only the first one.

1) Only one input string is provided.
2) Words are separated by spaces or line breaks {{\n}}.
3) Ignore capitalization when comparing words.
4) Words that contain non-alphabetic characters will count them as part of the word. E.g. "it's" is equivalent to "it's"
5) Ignore non-alphabetical characters at the beginning of a repeat group, or the end of the repeat group. E.g. "!repeat repeat repeat!" should output "repeat"
6) Do not ignore non-alphabetical characters inside of a repeat group. E.g. "hi! hi!" is not a repeat as it produces "hi!" and "hi" from rule 5.
7) When outputting a repeat group, print the first word exactly as it originally appears minus any non-alphabetical characters at the beginning.
8) Print each repeated word on its own line, in the order found.

Example:
Input:
Example example text Text text a , a!a. a ,a ,b b,

Output:
Example
text
b

Reasoning:
The first group of repeated words starts with "Example".
The second group of similar words starts with "text".
The third group is separated by special characters so isn't included. E.g. "a" != "," != "a!a." != "a" != ",a"
The fourth group of ",b b," can be considered a repeat as there are non-alphabetical characters surrounding it, but none in-between.

If there are no repeats, just write {{No repeats!}}.

Input
A single string to check for duplicates.

Output
Each repeated word on individual lines.
Or {{No repeats!}} if there aren't repeated words.

Constraints
Input string will only contain ASCII characters.

Words should only be considered when separated by spaces or '\n'. Any non-alphabetical characters should be considered part of the word except for the specific exception of non-alphabetical characters before the first word and after the last word.

Words that contain special characters but which should count as repeats (special characters before the first word or after the last word) won't contain alphabetical characters between special characters.
e.g. neither "@n@hi hi@n@" nor "@it's it's@" will appear.

Example:
Input:
Example example text Text text.

Output:
Example
text
Text

Game modes
Fastest, Shortest, Reverse

Test cases

Test 1 Test

Input
Example example text Text text.

Output
Example
text
Text

Validator 1 Validator

Input
Simple simple test for for this kind of of text Text text.\nOutput all repeated words, one on each line, in the order they're found. If there's capitalization differences, use the the first word of the two.

Output
Simple
for
of
text
Text
the

Test 2 Test

Input
Sometimes double words are grammatically correct. What it is is super annoying, but we'll have to check them anyway.

Output
is

Validator 2 Validator

Input
I had had too big a meal \n People should know that that kind of thing could exist and not be wrong.

Output
had
that

Test 3 Test

Input
No need to flag repeats when separated by punctuation. Punctuation separation is usually intentional. Even when you incorrectly do it ,it is probably just a typographical error and shouldn't be considered a repeat.

Output
No repeats!

Validator 3 Validator

Input
lie, lie ,lie. fie,fie.try, Try! try

Output
No repeats!

Test 4 Test

Input
Separating by a line might\nmight not be intentional, so it should be flagged. Even if it's \n it's meant to be a duplicate, it won't hurt to make sure.

Output
might
it's

Validator 4 Validator

Input
a\\na hold\\nthis toy\\toy run*nrun jump!jump forever\\nforever

Output
a
forever

Test 5 Test

Input
Solutions should be able to handle apostrophes in the word and punctuation that doesn't separate words, !as as those shouldn't shouldn't'!? stop the word from being listed as a repeat. It should only focus on whitespace or line breaks.

Output
as
shouldn't

Validator 5 Validator

Input
#!@#$%^&*(hi hi!@#$/%(*&^

Output
hi
