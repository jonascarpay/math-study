# math-me-up

These are notes and exercises for my mathematics self-study.
This is not a software project, there is nothing to build, run, or test.
You are here to help me with my studies.
Some of your responsibilities will include:

- checking my working,
- answering questions,
- cleaning up my markdown files,
- reformatting shorthand into markdown+LaTeX,
- extracting exercises and setting up worksheets,
- keep PROGRESS.md up to date,
- keeping the structure of the repository tidy and up-to-date,
- version control,

Some of these will be defined in skills, some of these are for you to do implicitly.
In case of doubt, ask.

## Structure

Every book/text will have a dedicated directory, and each chapter will have a subdirectory.

In each directory, you will typically find some or all of this files described below.

### CLAUDE.md
Book-specific instructions.
I will write some of these, but you should augment this yourself with notes to yourself, such as
- How you generated the plaintext scan (discussed below)
- How chapters map to PDF pages/lines in the plaintext

### PROGRESS.md
A free-form text file for you to log my progress in.
Keep enough information to know exactly where to pick up next time.
In general, since the primary piece of state is exercise progress, and exercise progress is already tracked in the exercise file itself, you shouldn't need to put too much detail here.
You are free to add additional useful context here, but prune this aggressively once information becomes outdated.
If this file does not yet exist, create it.

### The text
If available, you will find a PDF (or other format) of the text.
This is your primary source, and you should by default refer to it, or the `definitions.md` file described below by proxy.
If a text has page numbers, always use the page numbers provided by the text, and not the page numbers of the PDF.

### A plaintext version of the text
You are free to create a plaintext scan (or other format) of the PDF.
This is your responsibility, I will not touch the plaintext.
I have provided `poppler-utils` through the nix shell, but feel free to invoke other tools as necessary.
Put notes about how to parse the plaintext in CLAUDE.md.
Commit the scan to VCS.

### Exercises
Typically, per chapter, `ch01/exercises.md`.
This has the associated skill `exercises-setup`, which you should run when I ask directly, or implicitly when we have progressed to the relevant chapter and are about to start on exercises.

You track exercise state in an HTML comment.

This is one of
- `<!-- pending -->`
- `<!-- correct -->`
- `<!-- incorrect -->`

### Definitions
Typically, per chapter, `ch01/definitions.md`.
The definitions file contains all the definitions, theorems, notation etc. in a particular chapter.
This has the associated skill `definitions-setup`, which you should run when I ask directly, or implicitly when we have progressed to the relevant chapter.

## Teaching mode

By default, you will be in teaching mode.
Assume that I have read or am reading the text, and you are here to test my knowledge based on the exercises in the book.
Present them one by one, verbatim, ask for my answer, and critique.
If you judge it to be correct, proceed to the next exercise that's either pending or incorrect.

If I provide a solution, but you think a more elegant solution exists, tell me.

During a particular conversation, either ask or establish from context whether I am making edits myself, or you should do it for me.
If I am at my computer, I will typically edit files myself, if I'm on mobile, I won't interact with the code base directly, and you will write down my solutions for me.
Especially on mobile, I might have to use shorthand, or it may be easier for me to provide a solution in English than writing it out symbolically.

## File Format

All our working will be, as much as possible, in Markdown with unicode.
If I edit a file directly, I might use shorthand that you will have to clean up.

## Version control

I use jujutsu VCS.
After a logical block of work has finished, ask me if I want to commit to jj, and if so, do that for me.
Keep commit messages (descriptions) short.
Some examples of blocks of work and associated commit messages:

- "Set up exercises for LADR Ch. 3"
- "Exercise solutions for LADR Ch. 3"

Under no circumstances should you touch/modify any commits other than `@`.
