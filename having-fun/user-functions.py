def repeat(s, question):
    """
    Returns the user input repeated three times and
    if they include a third argument sys.argv[2]
    then it will add three question marks.
    """

    result = s * 3

    if question:
        result = result + "???"
    return result


def main():
    print 'We\'re just having fun!'
    print '-' * 20
    print repeat('Alright ', False)
    print repeat('Can You Hear Me ', True)

  
if __name__ == '__main__':
    main()
