import os
import argparse

# return all lines scanned.
def process(dir, langs=[], remove_first_comment=True, remove_comment=False):
  accept_all_file = False
  if 'all' in langs:
    accept_all_file = True
  dir_len = len(dir)
  documents = [] # { title: '', lines: []}

  def parse_file(file, cstyle_comment=True):
    try:
      # is binary?
      with open(file, "r") as textlines:
        fullpath = file.path
        relapath = fullpath[dir_len:]
        lines = []
        # ingores
        copyright_removed = False
        in_comments = False
        for line in textlines:
          # ingore empty line
          striped_line = line.strip()
          if len(striped_line) == 0:
            continue
          if remove_first_comment:
            if not copyright_removed:
              if cstyle_comment:
                if striped_line.startswith('//'):
                  continue
                if striped_line.startswith('/*'):
                  continue
                if striped_line.startswith('*'):
                  continue
                if striped_line.startswith('*/'):
                  continue
              else:
                if striped_line.startswith('#'):
                  continue
                if striped_line.startswith(';'):
                  continue
              copyright_removed = True
          # ingore comments
          if remove_comment:
            if cstyle_comment:
              if '*/' in striped_line:
                in_comments = False
                continue
              if in_comments:
                continue
              if '/*' in striped_line: # c-style lang
                if '*/' in striped_line:
                  # remove comment
                  comment_begin = striped_line.find('/*')
                  comment_end = striped_line.find('*/') + 2
                  if (comment_end - comment_begin <= len(striped_line)):
                    continue
                  else:
                    lines.append(line) # there exists codes except comment.
                    continue
                else:
                  in_comments = True
                continue
              if striped_line.startswith('//'): # c-style lang
                continue
            else:
              if striped_line.startswith(';'):  # python, elixir, ...
                continue
              if striped_line.startswith('#'):  # python, elixir, ...
                continue
          lines.append(line)
        print(f'\tfile: #lines={len(lines): >5}  {fullpath}')
        # print(f'\tline: {len(lines)}')
        documents.append((relapath, fullpath, lines))
    except UnicodeDecodeError:
      pass # Fond non-text data

  def scan_subdir(subdir):
    # print(f'\tpath: {subdir}')
    for file in os.scandir(subdir):
      if file.is_dir():
        scan_subdir(file.path)
      else:
        ext = file.name.split('.')[-1:][0]
        cstyle_comment = ext not in ['py', 'iex', 'ex']
        if accept_all_file:
          parse_file(file, cstyle_comment=cstyle_comment)
        else:
          if ext in langs:
            parse_file(file, cstyle_comment=cstyle_comment)

  scan_subdir(dir)
  return documents

def main():
  parser = argparse.ArgumentParser(
    prog='china-software-copyrighter',
    description='中国特色软件著作权代码生成器',
    epilog='Copyright(youxingz) © 2023'
  )
  parser.add_argument('-d', '--dir', required=True)
  parser.add_argument('-m', '--main', required=True, help='主函数入口所在文件')
  parser.add_argument('-o', '--out', default='output.docx')
  parser.add_argument('-l', '--languages', default='all', help='需要扫描的语言文件格式，用 "," 隔开')
  args = parser.parse_args()
  print(f'dir   = {args.dir}')
  print(f'main  = {args.main}')
  print(f'out   = {args.out}')
  print(f'langs = {args.languages}')
  docs = process(args.dir, args.languages.split(','), remove_first_comment=True, remove_comment=True)
  print(f'files = {len(docs)}')

if __name__ == '__main__':
  main()
