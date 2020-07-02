class MapNode:
	def __init__(self,key,value):
		self.key=key
		self.value=value
		self.next=None

class HashMap:

	def __init__(self,size):
		self.bucketSize=size
		self.bucket=[None for i in range(self.bucketSize)]
		self.count=0

	def getIndex(self,hc):
		return (abs(hc)%self.bucketSize)

	def size(self):
		return self.count

	def getValue(self,key):
		hc=hash(key)
		index=self.getIndex(hc)
		head=self.bucket[index]
		while head is not None:
			if head.key==key:
				return head.value
			head=head.next
		return None

	def insert(self,key,value):
		hc=hash(key)
		index=self.getIndex(hc)
		head=self.bucket[index]
		while head is not None:
			if head.key==key:
				head.value=value
				return
			head=head.next
		head=self.bucket[index]
		newNode=MapNode(key,value)
		newNode.next=head
		self.bucket[index]=newNode
		self.count +=1

		

	def remove(self,key):
		hc=hash(key)
		index=self.getIndex(hc)
		head=self.bucket[index]
		prev=None
		flag=False
		while head is not None:
			if head.key==key:
				flag=True
				if prev is None:
					self.bucket[index]=head.next
				else:
					prev.next=head.next

				self.count -=1
			prev=head
			head=head.next
		if flag:
			return  "Sucessful"
		else:
			return "No Element Found"
h=HashMap(10)



		


