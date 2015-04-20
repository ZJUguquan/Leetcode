# TODO: complete this class

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    collection = []

    items_per_page, m, n = 0, 0, 0
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

        self.m, self.n = divmod(len(collection), items_per_page)
        self.page_count = 0
        if self.n == 0 :
            self.page_count = self.m
        else :
            self.page_count = self.m + 1

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(instance):
        return self.page_count

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self,page_index):
        if page_index > self.page_count or page_index < 0:
            return -1
        if page_index < self.page_count:
            return self.m
        else:
            return self.n


    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self,item_index):
        if item_index > self.item_count() or item_index <0:
            return -1
        return (item_index) // self.items_per_page

    def __get__(self):
        return self.page_count

from pprint import pprint
helper = PaginationHelper(['a','b','c','d','e','f'], 4)

print(helper.page_index(2))
collection = range(1,25)
helper = PaginationHelper(collection, 10)
print(helper.page_count())


# print(PaginationHelper.page_count(helper))
# print(helper.page_count)
# print(helper.m, helper.n, PaginationHelper.__get__(page_count))
# print(
# helper.page_count, # should == 2
# helper.item_count, # should == 6
# helper.page_item_count(0),  # should == 4
# helper.page_item_count(1), # last page - should == 2
# helper.page_item_count(2), # should == -1 since the page is invalid
# # page_ndex takes an item index and returns the page that it belongs on
# helper.page_index(5), # should == 1 (zero based index)
# helper.page_index(2), # should == 0
# helper.page_index(20), # should == -1
# helper.page_index(-10)# should == -1 because negative indexes are invalid

# )


from math import ceil

# TODO: complete this class

class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
      self.collection=collection
      self.items=items_per_page

  # returns the number of items within the entire collection
  def item_count(self):
      return len(self.collection)

  # returns the number of pages
  def page_count(self):
      return int(ceil(self.item_count()/float(self.items)))

  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
      return self.items if page_index<self.page_count()-1 else self.item_count() % self.items if page_index==self.page_count()-1 else -1

  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
      return item_index/self.items if item_index<self.item_count() and item_index>=0 else -1