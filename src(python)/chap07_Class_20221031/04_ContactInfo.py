class ContactInfo:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def print_info(self):
        print(f'{self.name} : {self.email}')

if __name__ == '__main__':
    james = ContactInfo('야고보', 'u8yes@naver.com')
    simon = ContactInfo('베드로', 'u8yes@naver.com')

    james.print_info()
    simon.print_info()