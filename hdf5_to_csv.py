import os
import glob
import hdf5_getters
import csv

def main():
    outputFile = open('songs.csv', 'w')
    writer = csv.writer(outputFile)
    
    
    csvRowString="song_number,artist_familiarity,artist_hotttnesss,artist_id,artist_mbid,artist_playmeid,artist_7digitalid,artist_latitude,artist_longitude,artist_location,artist_name,release,release_7digitalid,song_id,song_hotttnesss,title,track_7digitalid,analysis_sample_rate,audio_md5,danceability,duration,end_of_fade_in,energy,key,key_confidence,loudness,mode,mode_confidence,start_of_fade_out,tempo,time_signature,time_signature_confidence,track_id,year"

    outputFile.write(csvRowString + "\n");
    csvRowString = ""  

    #################################################
    #Set the basedir here, the root directory from which the search
    #for files stored in a (hierarchical data structure) will originate
    basedir = "." # "." As the default means the current directory
    ext = ".H5" #Set the extension here. H5 is the extension for HDF5 files.
    #################################################

    #FOR LOOP
    songCount = 0
    for root, dirs, files in os.walk(basedir):        
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
            print(f)

            songH5File = hdf5_getters.open_h5_file_read(f)
            
            values=[songCount,
                hdf5_getters.get_artist_familiarity(songH5File),
                hdf5_getters.get_artist_hotttnesss(songH5File),
                hdf5_getters.get_artist_id(songH5File),
                hdf5_getters.get_artist_mbid(songH5File),
                hdf5_getters.get_artist_playmeid(songH5File),
                hdf5_getters.get_artist_7digitalid(songH5File),
                hdf5_getters.get_artist_latitude(songH5File),
                hdf5_getters.get_artist_longitude(songH5File),
                hdf5_getters.get_artist_location(songH5File),
                hdf5_getters.get_artist_name(songH5File),
                hdf5_getters.get_release(songH5File),
                hdf5_getters.get_release_7digitalid(songH5File),
                hdf5_getters.get_song_id(songH5File),
                hdf5_getters.get_song_hotttnesss(songH5File),
                hdf5_getters.get_title(songH5File),
                hdf5_getters.get_track_7digitalid(songH5File),
                hdf5_getters.get_analysis_sample_rate(songH5File),
                hdf5_getters.get_audio_md5(songH5File),
                hdf5_getters.get_danceability(songH5File),
                hdf5_getters.get_duration(songH5File),
                hdf5_getters.get_end_of_fade_in(songH5File),
                hdf5_getters.get_energy(songH5File),
                hdf5_getters.get_key(songH5File),
                hdf5_getters.get_key_confidence(songH5File),
                hdf5_getters.get_loudness(songH5File),
                hdf5_getters.get_mode(songH5File),
                hdf5_getters.get_mode_confidence(songH5File),
                hdf5_getters.get_start_of_fade_out(songH5File),
                hdf5_getters.get_tempo(songH5File),
                hdf5_getters.get_time_signature(songH5File),
                hdf5_getters.get_time_signature_confidence(songH5File),
                hdf5_getters.get_track_id(songH5File),
                hdf5_getters.get_year(songH5File)]
            songH5File.close()
            songCount = songCount + 1

            writer.writerow(values)
            

    outputFile.close()
	
main()
