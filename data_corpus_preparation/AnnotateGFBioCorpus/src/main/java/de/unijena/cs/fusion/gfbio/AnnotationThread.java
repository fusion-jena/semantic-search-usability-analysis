package de.unijena.cs.fusion.gfbio;


import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.OutputStreamWriter;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Set;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import gate.AnnotationSet;
import gate.Corpus;
import gate.CorpusController;
import gate.Document;
import gate.Factory;



public class AnnotationThread implements Runnable {
    
	private static final Logger logger = LoggerFactory.getLogger(AnnotationThread.class);
	
	/** 
	   * List of annotation types to write out.  If null, write everything as
	   * GateXML.
	   */
	private static List annotTypesToWrite = null;
	
	/**
	   * The character encoding to use when loading the docments.  If null, the
	   * platform default encoding is used.
	   */
	  private static String encoding = "UTF-8";
	
	String threadName; //name of the thread

	
	
	File corpusFolder; //corpus folder
	String outputPath; //path to folder containing the annotated files
	

	CorpusController organismTagger; //OrganismTagger 
	CorpusController biodivTagger; //pennBioTagger 

    AnnotationThread(String threadName, File corpusFolder, String outputPath, CorpusController organismTagger, CorpusController biodivTagger) {
        this.threadName = threadName;
        
    	this.corpusFolder = corpusFolder;
        this.outputPath = outputPath;
        
 
        this.organismTagger = organismTagger;
        this.biodivTagger = biodivTagger;
    }

   
	public void run() {
    	
		try {
			Corpus corpus = Factory.newCorpus("BatchProcessApp Corpus");
			
			//assign corpus to tagger
			organismTagger.setCorpus(corpus);
			biodivTagger.setCorpus(corpus);
	
		    // process the files one by one
		    for(final File docFile : corpusFolder.listFiles()) {
		      // load the document (using the specified encoding if one was given)
		      
		      System.out.print("Processing document " + docFile + "...");
		      Document doc = Factory.newDocument(docFile.toURL(), encoding);
	
		      // put the document in the corpus
		      corpus.add(doc);
		      
		      // run the application	      
		      biodivTagger.execute();
		      organismTagger.execute();
	
		      // remove the document from the corpus again
		      corpus.clear();
	
		      String docXMLString = null;
		      // if we want to just write out specific annotation types, we must
		      // extract the annotations into a Set
		      if(annotTypesToWrite != null) {
		        // Create a temporary Set to hold the annotations we wish to write out
		        Set annotationsToWrite = new HashSet();
		        
		        // we only extract annotations from the default (unnamed) AnnotationSet
		        // in this example
		        AnnotationSet defaultAnnots = doc.getAnnotations();
		        Iterator annotTypesIt = annotTypesToWrite.iterator();
		        while(annotTypesIt.hasNext()) {
		          // extract all the annotations of each requested type and add them to
		          // the temporary set
		          AnnotationSet annotsOfThisType =
		              defaultAnnots.get((String)annotTypesIt.next());
		          if(annotsOfThisType != null) {
		            annotationsToWrite.addAll(annotsOfThisType);
		          }
		        }
	
		        // create the XML string using these annotations
		        docXMLString = doc.toXml(annotationsToWrite);
		      }
		      // otherwise, just write out the whole document as GateXML
		      else {
		        docXMLString = doc.toXml();
		      }
	
		      // Release the document, as it is no longer needed
		      Factory.deleteResource(doc);
	
		      // output the XML to <inputFile>.out.xml
		      String outputFileName = this.outputPath+docFile.getName();
		      File outputFile = new File(outputFileName);
	
		      // Write output files using the same encoding as the original
		      FileOutputStream fos = new FileOutputStream(outputFile);
		      BufferedOutputStream bos = new BufferedOutputStream(fos);
		      OutputStreamWriter out;
		      if(encoding == null) {
		        out = new OutputStreamWriter(bos);
		      }
		      else {
		        out = new OutputStreamWriter(bos, encoding);
		      }
	
		      out.write(docXMLString);
		      
		      out.close();
		      System.out.println("done");
		    } // for each file

		}
		catch(Exception e){
			e.printStackTrace();
		}
	
         
         
    }

	
	
	
	 public String getOutputPath() {
			return outputPath;
		}

	public void setOutputPath(String outputPath) {
		this.outputPath = outputPath;
	}

	public String getThreadName() {
		return threadName;
	}


	public void setThreadName(String threadName) {
		this.threadName = threadName;
	}

	
	
}
