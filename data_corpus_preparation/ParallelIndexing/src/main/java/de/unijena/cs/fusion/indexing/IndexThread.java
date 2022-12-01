package de.unijena.cs.fusion.indexing;


import java.io.File;
import java.net.URL;


import gate.CorpusController;
import gate.Document;
import gate.Factory;
import gate.mimir.index.MimirConnector;



public class IndexThread implements Runnable {
 	
	/**
	   * The character encoding to use when loading the docments.  If null, the
	   * platform default encoding is used.
	   */
	  private static String encoding = "UTF-8";
	
	String threadName; //name of the thread
	
	String indexURL;

	
	
	File corpusFolder; //corpus folder

	
    IndexThread(String threadName, File corpusFolder, String indexURL) {
        this.threadName = threadName;
        
    	this.corpusFolder = corpusFolder;
       
        this.indexURL = indexURL;
    }

   
	public void run() {
    	
		try {
			
			MimirConnector connector = new MimirConnector(new URL(indexURL));
			
		    // process the files one by one
		    for(final File docFile : corpusFolder.listFiles()) {
		      // load the document (using the specified encoding if one was given)
		      
		      System.out.print("Processing document " + docFile + "...");
		      Document doc = Factory.newDocument(docFile.toURL(), encoding);
	
		    
		  	  // index the document
		      connector.sendToMimir(doc, null);
		    
		      // Release the document, as it is no longer needed
		      Factory.deleteResource(doc);
	
		     	      
		      
		      System.out.println("done");
		    } // for each file
		    
		    //close the connector
		    connector.close();

		}
		catch(Exception e){
			e.printStackTrace();
		}
	
         
         
    }

	
	
	
	public String getThreadName() {
		return threadName;
	}


	public void setThreadName(String threadName) {
		this.threadName = threadName;
	}

	
	
}
