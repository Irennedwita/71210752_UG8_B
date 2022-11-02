#program untuk menampilkan queue dan circular queue dimana terdapat hapus data, tambah data, dan display data

class CircularQueue:

    def __init__(self,cap):
        self.data = []
        self.size = 0
        self.front = -1
        self.capacity = cap

    def enqueue(self,e):
        if self.size < self.capacity:
            self.data.append(e)
            self.size = self.size + 1
            self.front = 0
        else:
            print("Penuh!")

    def dequeue(self):
        if self.size > 0:
            hasil = self.data[self.front]
            self.data.pop(self.front)
            self.size = self.size - 1
        else:
            print("Kosong!")
        return hasil

    def display(self):
        if self.size >= self.capacity:
            print("Yang ada pada antrian circular adalah: ", end=" ")
            for e in self.data:
                print(e,"", end="")
            print()
            print("Antrian Penuh")
        else:
            print("Yang ada pada antrian adalah: ", end=" ")
            for e in self.data:
                print(e,"", end="")
            print()

circularQueue = CircularQueue(5)
circularQueue.enqueue(14)
circularQueue.enqueue(22)
circularQueue.enqueue(13)
circularQueue.enqueue(-6)
circularQueue.display()
print("Data yang dihapus adalah = ", circularQueue.dequeue())
print("Data yang dihapus adalah = ", circularQueue.dequeue())
circularQueue.display()
circularQueue.enqueue(9)
circularQueue.enqueue(20)
circularQueue.enqueue(5)
circularQueue.display()

