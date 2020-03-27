import argparse, shutil, os

# Usage: python init_new_chapter.py 5

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Initialize the folder structure, base files, and commit of a new chapter.")
    parser.add_argument(
        'chapter_num', type=int, help="The chapter number"
    )
    args = parser.parse_args()
    chapter_num_str = str(args.chapter_num)
    if args.chapter_num < 10: 
        chapter_num_str = '0' + chapter_num_str

    source_folder_path = os.path.dirname(os.path.abspath(__file__)) + '\\css_mm_4e\\css_mm_4e-master\\' + chapter_num_str
    dest_folder_path = os.path.dirname(os.path.abspath(__file__)) + '\\ch' + str(args.chapter_num)

    print("Source folder path: " + source_folder_path)
    print("Destination folder path: " + dest_folder_path)

    print("Copying from source to destination.")
    shutil.copytree(source_folder_path, dest_folder_path)

    git_commit_cmd = 'git add ch' + str(args.chapter_num) + '/ && git commit -m "ch' + str(args.chapter_num) + ': adding base files"'

    print("Git commit command: " + git_commit_cmd)

    os.system(git_commit_cmd)


