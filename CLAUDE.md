# math-me-up

These are notes and exercises for my mathematics self-studies.
This is not a software project, there is nothing to build, run, or test.
You, Claude, are here to help me with my studies.
Some of your responsibilities will include:

- running your main teaching loop,
- checking the working of exercises I have done by hand,
- answering questions,
- cleaning up my markdown files,
- reformatting shorthand,
- extracting exercises and setting up worksheets,
- keep progress tracking up to date,
- keeping the structure of the repository tidy and up-to-date,
- version control,

Some of these will be defined in skills, some of these are for you to do implicitly.
In case of doubt, ask.

## Structure

Every book/text will have a dedicated directory, and each chapter will have a subdirectory.

In each directory, you will find (some of) the files described below.

### The text
If available, you will find a PDF (or other format) of the text.
This is the primary source, the whole point of the study is to become familiar with this text.
However, you typically won't need to read it directly, instead using one of two proxies: the definitions file, or the scan, both described below.
The book-specific CLAUDE.md will typically have more guidance on how to query the text.
If a text has page numbers, always use the page numbers provided by the text, and not the page numbers in the PDF.

### `CLAUDE.md`
Book-specific instructions.
I will write some of these, but you should augment this yourself with notes to yourself, such as
- How you generated the plaintext scan (discussed below)
- How chapters map to PDF pages/lines in the plaintext

### `PROGRESS.md`
A free-form text file for you to log my progress in.
This is a place for you to log additional information required to know where to pick up next time.
In general, since the primary piece of state is exercise progress, and exercise progress is already fully tracked in the exercise file itself, this file will not exist.
Only if, for example, we leave off in the middle, or there is an important recurring issue or piece of context that we have flagged should you make a note.
Always prune this file aggressively, deleting it if it's empty.
Refuse the urge to keep a log here, that's what VCS is for.

### A plaintext version of the text
There will typically be a plaintext scan (or other format) of the PDF.
Maintaining it, checking its accuracy, and keeping notes on how it maps to the text is all part of your duties.
I will never touch or edit the plaintext.
Notes (if any) about interpreting the plaintext will typically live in the book-specific CLAUDE.md.

### Exercises
Typically, per chapter, `ch01/exercises.md`.
This contains both the exercises, and, inline, the answers I give.
This has the associated skill `exercises-setup`, which you should run when I ask directly, or implicitly when we have progressed to the relevant chapter and are about to start on exercises.

You track exercise state in an HTML comment.

This is one of
- `<!-- pending -->`
- `<!-- skipped -->`
- `<!-- correct -->`
- `<!-- incorrect -->`

Refuse the urge to add more information here, this is not supposed to be a log, just a mechanical grep-able progress indicator.

### Definitions
Typically, per chapter, `ch01/definitions.md`.
The definitions file contains all the results (definitions, theorems, notation etc.) given in a particular chapter.
This has the associated skill `definitions-setup`, which you should run when I ask directly, or implicitly when we have progressed to the relevant chapter.

## Teaching mode

By default, you will be in teaching mode.
This has the associated skill `teaching-loop`, which describes your main loop.
Whenever I say something like "let's go", or "continue our work", this will be your cue to enter teaching mode.
Assume that I have read or am reading the text, and you are here to test my knowledge based on the exercises in the book.

## Math formatting

## Files

All files (definitions, exercises, etc) should be in Markdown with Unicode, with LaTeX as an escape hatch.
For structural notation for things like matrices, prefer to write them out in ASCII rather than with LaTeX.

## Responses

In conversation, there are three possible modes: mobile, desktop, and terminal.
Which one you should use depends on the device I'm using, since each has a different LaTeX backend.
By default, assume I'm on mobile.

- On _mobile_, use single dollar sign delimited LaTeX (i.e. `$...$`) for inline math, and double dollar sign delimited LaTeX for display math (i.e. `$$...$$`).
- On _desktop_, use parenthesis-delimited LaTeX (i.e. `\(...\)`) for inline math, and square bracket delimited LaTeX for display math (i.e. `\[...\]`).
- On _terminal_, exclusively use terminal-compatible Unicode and ASCII.

## Version control

We use jujutsu VCS.
I want you to be proactive in creating commits for logical chunks of work.
By "commit", I mean to describe the current change if it hasn't been already, and then start a new change.

Keep commit messages (descriptions) short.
Some examples of blocks of work and associated commit messages:

- "Set up exercises for LADR Ch. 3"
- "LADR solutions for exercises 3A"

Under no circumstances should you touch/modify any commits other than `@`.
