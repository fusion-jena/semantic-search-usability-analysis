package de.unijena.cs.fusion.gfbio;

import java.io.File;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import gate.CorpusController;
import gate.Gate;

public class AnnotateGFBio {

	private static final Logger logger = LoggerFactory.getLogger(AnnotateGFBio.class);
	public static final String PATH_TO_BiodivTAGGER = "F:\\userevaluation\\Pipeline\\BT8.6\\application.xgapp";
	private static final String PATH_TO_OrganismTAGGER = "F:\\biodiv-gold-standard\\OT8.6\\application.xgapp";

    //public static final String PATH_TO_BiodivTAGGER = "/home/felicitas/repository/code/pipelines/BT86withDiseases/application.xgapp";
	//private static final String PATH_TO_OrganismTAGGER = "/home/felicitas/repository/biodiv-gold-standard/OT8.6/application.xgapp";
	
	public static final String PATH_TO_GFBIO1 = "F:\\userevaluation\\Data\\output\\corpus1";
	public static final String PATH_TO_GFBIO2 = "F:\\userevaluation\\Data\\output\\corpus2";
	private static final String OUTPUT1 = "F:\\userevaluation\\Data\\output_annotated\\corpus1\\";
	private static final String OUTPUT2 = "F:\\userevaluation\\Data\\output_annotated\\corpus2\\";
	
	//public static final String PATH_TO_GFBIO1 = "/home/felicitas/repository/data/BioCADDIE/BioCADDIE_splitted2/corpus5";
	//public static final String PATH_TO_GFBIO2 = "/home/felicitas/repository/data/BioCADDIE/BioCADDIE_splitted2/corpus5";
	
	//private static final String OUTPUT1 = "/home/felicitas/data3/bioCADDIE/corpus5_annotated/";
	//private static final String OUTPUT2 = "/home/felicitas/data3/bioCADDIE/corpus5_annotated/";
	
	/** 
	   * List of annotation types to write out.  If null, write everything as
	   * GateXML.
	   */
	private static List annotTypesToWrite = null;
	
	/**
	   * The character encoding to use when loading the docments.  If null, the
	   * platform default encoding is used.
	   */
	  private static String encoding = null;
	  

	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		try{
			Gate.init();
			logger.info("Gate initialized");
			

			File gfbio1 = new File(PATH_TO_GFBIO1);
			File gfbio2 = new File(PATH_TO_GFBIO2);
			
			File organismTaggerFolder = new File(PATH_TO_OrganismTAGGER);
			File biodivTaggerFolder = new File(PATH_TO_BiodivTAGGER);
			
			
				
			//create two instance of the pipeline for multithreading
			CorpusController organismTagger1 = (CorpusController) gate.util.persistence.PersistenceManager. 
	                loadObjectFromFile(organismTaggerFolder);
			CorpusController organismTagger2 = (CorpusController) gate.util.persistence.PersistenceManager. 
	                loadObjectFromFile(organismTaggerFolder);

			System.out.println("organismTagger initialized");
			
			//create two instance of the pipeline for multithreading
			CorpusController biodivTagger1 = (CorpusController) gate.util.persistence.PersistenceManager. 
	                loadObjectFromFile(biodivTaggerFolder);
			CorpusController biodivTagger2 = (CorpusController) gate.util.persistence.PersistenceManager. 
	                loadObjectFromFile(biodivTaggerFolder);

			System.out.println("biodivTagger initialized");
			
			//first thread
			AnnotationThread firstThread = new AnnotationThread("Thread1", gfbio1, OUTPUT1, organismTagger1,biodivTagger1);
	        
	    	new Thread(firstThread).start();
	    	System.out.println("first thread started");
	    	
	    	//second thread
	    	AnnotationThread secondThread = new AnnotationThread("Thread2", gfbio2, OUTPUT2, organismTagger2,biodivTagger2);
	        
	    	new Thread(secondThread).start();
	    	System.out.println("second thread started");

			
		}catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	

}
