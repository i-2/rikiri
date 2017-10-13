## Rikiri

Rikiri let's you to compose html presentations with markdown files or another static files, although it's scope is currently restricted to markdown for now.

## Installation

```
pip install rikiri

```

## Usage

```
usage: rikiri [-h] [-t TITLE] [-o OUTDIR] [-s SOURCEDIR]

Make github HTML presentation like a boss

optional arguments:
  -h, --help            show this help message and exit
  -t TITLE, --title TITLE
                        title of the presentation
  -o OUTDIR, --outdir OUTDIR
                        output directory
  -s SOURCEDIR, --sourcedir SOURCEDIR
                        Source directory

```

If you have markdown files stored in a particular directory then you can convert it into html presentation with a help of below command.

```
.
├── source
│   ├── file11.md
│   └── file12.md
└── README.md
```

```
rikiri -t <title_of_presentation> -s <source_dir>

```

## LICENSE

MIT