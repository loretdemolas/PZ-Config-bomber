def status(Comment1, Comment2 = '', Comment3 = '',Comment4=''):
       # Determine the length of the comment text
    comment_length = max(len(Comment1),len(Comment2),len(Comment3))

    # Set the length of the header and footer to be the same as the length of the comment plus 6
    header_footer_length = comment_length + 6

    # Print the header
    print("#" * header_footer_length)
    print()

    # Print the comment with padding on either side
    print("# {:{}} #".format(Comment1, comment_length))
    print()
    if Comment2 != '':
        print("# {:{}} #".format(Comment2, comment_length))
        print()
    if Comment3 != '':
        print("# {:{}} #".format(Comment3, comment_length))
        print()
    if Comment4 != '':
        print("# {:{}} #".format(Comment4, comment_length))
        print()
    

    # Print the footer
    print("#" * header_footer_length)