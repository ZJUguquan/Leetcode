def pagination_text(page_number, page_size, total_products):
    m, n = divmod(total_products, page_size)
    s = 'Showing {f} to {s} of {t} Products.'
    if page_number <= m:
        return s.format(f=(page_number-1)*page_size +1, s=page_number*page_size, t=total_products)
    else:
        return s.format(f=(page_number-1)*page_size +1, s=total_products, t=total_products)



print pagination_text(1,10,30)
print pagination_text(3,10,26)
print pagination_text(1,10,8)
print pagination_text(2,30,350)
print pagination_text(1,23,30)
print pagination_text(2,23,30)
print pagination_text(43,15,3456)