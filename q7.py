import glob
import re

BLOCK_COMMENT_START_PATTERN = re.compile(r'^\s*""".*?$')
BLOCK_COMMENT_END_PATTERN = re.compile(r'^.*?"""$')
COMMENT_PATTERN = re.compile(r'^\s*\#.*$')
BLANK_LINE_PATTERN = re.compile(r'^\s*$')


def code_count(file_pattern):
    """
    Count line in code file
    :param file_pattern: fnmatch type pattern
    :return: (code_line, comment_line, blank_line)
    """
    code_lines = 0
    comment_lines = 0
    blank_lines = 0
    is_comment = False
    files = glob.glob(file_pattern)
    for file in files:
        with open(file) as fp:
            for line in fp:
                if not is_comment:
                    if COMMENT_PATTERN.match(line):
                        comment_lines += 1
                    elif BLANK_LINE_PATTERN.match(line):
                        blank_lines += 1
                    elif BLOCK_COMMENT_START_PATTERN.match(line):
                        comment_lines += 1
                        is_comment = True
                    else:
                        code_lines += 1
                else:
                    comment_lines += 1
                    if BLOCK_COMMENT_END_PATTERN.match(line):
                       is_comment = False
    return (len(files), code_lines, comment_lines, blank_lines)


if __name__ == '__main__':
    files, code_lines, comment_lines, blank_lines = code_count('*.py')
    print 'Summary in {} files'.format(files)
    print 'Code Lines: {}'.format(code_lines)
    print 'Comment Lines: {}'.format(comment_lines)
    print 'Blank Lines: {}'.format(blank_lines)
