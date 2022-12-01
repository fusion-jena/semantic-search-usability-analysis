package de.unijena.cs.fusion.indexing;

import java.io.File;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import gate.Gate;

public class IndexingGFBio{

	private static final Logger logger = LoggerFactory.getLogger(IndexingGFBio.class);
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		try{
			Gate.init();
			logger.info("Gate initialized");
			File gfbioCorpus = null;
			String indexURL = null;
			
			if(args[0] == null | args[1] == null){
				System.out.println("Please provide at least one corpus path (arg[0]) and an index URL (arg[1]).");
				System.exit(0);
			}
			
			
			if(args[0]!=null){
			  gfbioCorpus = new File(args[0]);
			}
			if(args[1]!=null){
				indexURL = args[1];
			}
			
			
			if(gfbioCorpus!=null){			
			  //first thread
			   IndexThread firstThread = new IndexThread("Thread1", gfbioCorpus, indexURL);
	        
	    	   new Thread(firstThread).start();
	    	   System.out.println("first thread started");
		      }
	    	
		
			
		}catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	

}
