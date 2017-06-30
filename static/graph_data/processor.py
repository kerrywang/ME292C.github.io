import csv
import numpy as np

class OriginData(object):
	"""docstring for OriginData"""
	def __init__(self, filename):
		super(OriginData, self).__init__()
		self.filename = "../data/" + filename
		# For ME110_2
		self.filename = "../data/ME110_2/" + filename
		self.des_filename = filename
		self.concept_list = list()
		self.graph_data()
		

	def graph_data(self):
		xindices, yindices, human_label_list, machine_label_list = self.readcsv()
		convx, convy = self.get_sorted_idx(xindices, yindices)
		self.get_sorted_graph(convx, xindices, human_label_list, convy, yindices, machine_label_list)
		# print (convx)
		# print (convy)

	def readcsv(self):
		with open(self.filename) as csvfile:
			firstline = True
			reader = csv.reader(csvfile)
			human_label_list = list()
			machine_label_list = list()
			xindices = list()
			yindices = list()
			for row in reader:
				if firstline:
					firstline = False
					continue
				row[3] = row[3].strip()
				if row[3] not in human_label_list:
					human_label_list.append(row[3])
				if row[4] not in machine_label_list:
					machine_label_list.append(row[4])
				self.concept_list.append({'concept_index':row[0],
					'human_label':row[3],
					'human_label_index':(human_label_list.index(row[3])),
					'machine_label':row[4],
					'machine_label_index':machine_label_list.index(row[4])})
				xindices.append(human_label_list.index(row[3]))
				yindices.append(machine_label_list.index(row[4]))

			return xindices, yindices,human_label_list, machine_label_list

	def get_sorted_idx(self,xindices, yindices):
		nx = max(xindices)+1
		ny = max(yindices)+1

		cnt = np.zeros([ny, nx])
		for x, y in zip(xindices, yindices):
				cnt[y,x] += 1
		chk = cnt.copy()

		oldx = list(range(nx))
		oldy = list(range(ny))
		newx = []
		newy = []
		while len(oldx)*len(oldy) > 1:
			r, c = np.unravel_index(np.argmax(chk), chk.shape)
			if len(oldx)>1: 
				newx.append(oldx.pop(c))
				chk = np.delete(chk, c, axis=1)
			if len(oldy)>1: 
				newy.append(oldy.pop(r))
				chk = np.delete(chk, r, axis=0)
		newx += oldx
		newy += oldy
		
		converterx = {old:newx.index(old) for old in range(nx)}
		convertery = {old:newy.index(old) for old in range(ny)}
		return converterx, convertery

	def get_sorted_graph(self,convx, xindices, human_label_list, convy, yindices, machine_label_list):

		xindices = [convx[x] for x in xindices]
		yindices = [convy[y] for y in yindices]

		# print (convy)
		# print (machine_label_list)

		xticklabels_ = human_label_list[:]
		for i, tl in enumerate(human_label_list): xticklabels_[convx[i]] = tl
		human_label_list = xticklabels_

		yticklabels_ = machine_label_list[:]
		for i, tl in enumerate(machine_label_list): yticklabels_[convy[i]] = tl
		machine_label_list = yticklabels_

		print (machine_label_list)

		nx = max(xindices) + 1
		ny = max(yindices) + 1
		cnt = np.zeros([nx,ny])
		concept_indices = dict()

		for i,pos in enumerate(zip(xindices,yindices)):
			cnt[pos[0],pos[1]] += 1
			if (pos[0],pos[1]) not in concept_indices.keys():
				concept_indices[(pos[0],pos[1])] = list()
			concept_indices[(pos[0],pos[1])].append(i+1)


		with open(self.des_filename,'wb') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',',
								quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow(['Human_Label_Index','Human_Label',"Machine_Label_Index", "Machine_Label","Bubble_size","Concept_Indices"])
			for pos in concept_indices: 

				spamwriter.writerow([pos[0],human_label_list[pos[0]], pos[1], machine_label_list[pos[1]], len(concept_indices[pos]), str(concept_indices[pos]).replace(',',';')])
		
		with open("Mapping_"+self.des_filename,'wb') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',',
								quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow(["Index","Human_Label","Machine_Label"])
			print (len(human_label_list),len(machine_label_list))
			for i in range(len(human_label_list)):
				spamwriter.writerow([i,human_label_list[i], machine_label_list[i]])






if __name__ == '__main__':
	# od = OriginData("Human_manchine_details_des_Team1.csv")
	# od = OriginData("ME110_HM_Team14.csv")

	# od.graph_data()

	# ME110_2
	od = OriginData("ME110_2_HM_Team10.csv")

				




