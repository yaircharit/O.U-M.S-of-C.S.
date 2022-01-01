import h5py

db = h5py.File('fonts_data.hdf5')
im_names = list(db.keys())

im = im_names[0]
img = db[im][:]
font = db[im].attrs['font']
# txt = db['data'][im].attrs['txt']
# charBB = db['data'][im].attrs['charBB']
# wordBB = db['data'][im].attrs['wordBB']
print(img)