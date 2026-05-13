# CodingGame_Clash_Submission
I submitted a problem to codingame, but it might need to be made simpler, so I want to record it here.



Goal

When proofreading, some people have a hard time time seeing repeats, especially if they're broken up onto different lines. The brain just ignores them.

Print all of the repeated words found in a string, one on each line, to help find such words when editing text.

Words are separated by spaces or line breaks.
Ignore capitalization when comparing words.
Ignore non-alphabetical characters at the start or end of a word.
Special characters between words counts as separating them, so those words should not be considered repeats.
When outputting a repeated pair, print the first word exactly as it originally appears.
Print each repeated word on its own line, in the order found.

Example:
Input:
text Text text

Output:
text
Text

Reasoning:
the first pair of repeats is "text Text" so output "text".
The second pair of repeats is "Text text" so output "Text".

If there are no repeats, just write {{No repeats!}}.

Input
A string to check for duplicates.

Output
Each repeated word on individual lines.
Or {{No repeats!}} if there aren't repeated words.

Constraints
Input string will only contain ASCII characters.
Valid repeated words won't be separated by both punctuation and whitespace. e.g. "??a a??a" will not appear
Non-separating special characters won't contain alphabetical characters. e.g. "!@#JK#$%hi hi!!e!" will not appear

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
