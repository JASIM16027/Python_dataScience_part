
books_read = {'January': 'Think and grow rich', 'February': 'Power of subconscious mind', 'March': 'Four hour week',
              'April': 'Rich dad and poor dad', 'May': 'Alchemist', 'June': 'You can win'}

books = books_read    # alias create/ copy dictionary
books['April'] = 'Machine Learning'
books['july'] = 'Deep learning'

print(books_read['April'])
print(books_read['july'])
