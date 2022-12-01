package uni_jena.cs.fusion.GFBioDocumentFormat;

import java.util.ArrayList;

import gate.Annotation;
import gate.AnnotationSet;
import gate.Document;
import gate.Resource;
import gate.corpora.MimeType;
import gate.corpora.XmlDocumentFormat;
import gate.creole.ResourceInstantiationException;
import gate.creole.metadata.AutoInstance;
import gate.creole.metadata.CreoleResource;
import gate.util.DocumentFormatException;
import gate.util.InvalidOffsetException;


/**
 * UIMA XCAS and XMICAS document formats.
 */
@CreoleResource(name = "GFBio Document Format", isPrivate = true,
    autoinstances = {@AutoInstance(hidden = true)})
public class GFBioDocumentFormat extends XmlDocumentFormat {

  private static final long serialVersionUID = -3804187336078120808L;

  @Override
  public void unpackMarkup(Document doc) throws DocumentFormatException {
    super.unpackMarkup(doc);
    unpackCasMarkup(doc);
  }

  /**
   * Convert GFBio markups to GATE markups.
   * @param doc XML document already parsed
   * @throws DocumentFormatException error when parsing the file
   */
  private void unpackCasMarkup(Document doc)
    throws DocumentFormatException {

    AnnotationSet inputAS = doc.getAnnotations("Original markups");
    AnnotationSet outputAS = doc.getAnnotations("Original markups");
    
   ArrayList<String> authors = new ArrayList<String>();
   ArrayList<String> contributors = new ArrayList<String>();
   ArrayList<String> keywords = new ArrayList<String>();
  
   ArrayList<String> dataTypes = new ArrayList<String>();
   ArrayList<String> taxons = new ArrayList<String>();
   ArrayList<String> relatedDatasets = new ArrayList<String>();
   ArrayList<String> parameters = new ArrayList<String>();
   
   String title = "";
   String citation = "";
   String description = "";
   String collectionStartDate = "";
   String collectionEndDate = "";
   String publicationDate = "";
   String docId = "";
   String dataCenter = "";
   String access = "";
   String linkage = "";
   String northBoundLatitude = "";
   String southBoundLatitude = "";
   String eastBoundLongitude = "";
   String westBoundLongitude = "";
   String additionalContent = "";
    
    for (Annotation annotation : inputAS) {
    	//System.out.println(annotation.getType());
        if (annotation.getType().matches("dc:author") || annotation.getType().matches("dc:creator")) {
          try {
            String author = doc.getContent().getContent(
              annotation.getStartNode().getOffset(),
              annotation.getEndNode().getOffset()).toString();
            // add contained values as a feature to the array annotation
            if (!author.trim().equals("")) {
              authors.add(author);
            }
          } catch (InvalidOffsetException e) {
            throw new DocumentFormatException(e);
          }
        }
        if (annotation.getType().matches("dc:contributor")) {
            try {
              String contributor = doc.getContent().getContent(
                annotation.getStartNode().getOffset(),
                annotation.getEndNode().getOffset()).toString();
              // add contained values as a feature to the array annotation
              if (!contributor.trim().equals("")) {
                contributors.add(contributor);
              }
            } catch (InvalidOffsetException e) {
              throw new DocumentFormatException(e);
            }
          }
        
        if (annotation.getType().matches("dc:subject")) {
            try {
              if(annotation.getFeatures().get("type").equals("kingdom")) {
            	  String kingdom = doc.getContent().getContent(
                          annotation.getStartNode().getOffset(),
                          annotation.getEndNode().getOffset()).toString();
                        // add contained values as a feature to the array annotation
                        if (!kingdom.trim().equals("")) {
                          taxons.add(kingdom);
                        }
              }else if(annotation.getFeatures().get("type").equals("taxonomy")) {
            	  String taxonomy = doc.getContent().getContent(
                          annotation.getStartNode().getOffset(),
                          annotation.getEndNode().getOffset()).toString();
                        // add contained values as a feature to the array annotation
                        if (!taxonomy.trim().equals("")) {
                          taxons.add(taxonomy);
                        }
              }else if(annotation.getFeatures().get("type").equals("parameter")) {
            	  String parameter = doc.getContent().getContent(
                          annotation.getStartNode().getOffset(),
                          annotation.getEndNode().getOffset()).toString();
                        // add contained values as a feature to the array annotation
                        if (!parameter.trim().equals("")) {
                          parameters.add(parameter);
                        }
              }
              //method, sensor, feature, project only!
              else if (annotation.getFeatures().get("type").equals("method")||
            		  annotation.getFeatures().get("type").equals("sensor")||
            		  annotation.getFeatures().get("type").equals("project")){
            	  String keyword = doc.getContent().getContent(
                          annotation.getStartNode().getOffset(),
                          annotation.getEndNode().getOffset()).toString();
                        // add contained values as a feature to the array annotation
                        if (!keyword.trim().equals("")) {
                          keywords.add(keyword);
                        }
              }
              
            } catch (InvalidOffsetException e) {
              throw new DocumentFormatException(e);
            }
          }
        
        if (annotation.getType().matches("dc:title")) {
        	try {
				title = doc.getContent().getContent(
				        annotation.getStartNode().getOffset(),
				        annotation.getEndNode().getOffset()).toString();
			} catch (InvalidOffsetException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
        	
        }
        
        if (annotation.getType().matches("dc:source")) {
        	try {
				citation = doc.getContent().getContent(
				        annotation.getStartNode().getOffset(),
				        annotation.getEndNode().getOffset()).toString();
			} catch (InvalidOffsetException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
        	
        }
        
        if (annotation.getType().matches("dc:description")) {
        	try {
				description = doc.getContent().getContent(
				        annotation.getStartNode().getOffset(),
				        annotation.getEndNode().getOffset()).toString();
			} catch (InvalidOffsetException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
        	
        }
        
         
        //collection startDate
        if (annotation.getType().matches("startDate")) {
        	try {
				collectionStartDate = doc.getContent().getContent(
				        annotation.getStartNode().getOffset(),
				        annotation.getEndNode().getOffset()).toString();
				
			} catch (InvalidOffsetException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
        	
        }
        
      //collection endDate
        if (annotation.getType().matches("endDate")) {
        	try {
				collectionEndDate = doc.getContent().getContent(
				        annotation.getStartNode().getOffset(),
				        annotation.getEndNode().getOffset()).toString();
				
			} catch (InvalidOffsetException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
        	
        }
      //publicationDate
        
        if (annotation.getType().matches("dc:date")) {
            try {
              publicationDate = doc.getContent().getContent(
                annotation.getStartNode().getOffset(),
                annotation.getEndNode().getOffset()).toString();
              
            } catch (InvalidOffsetException e) {
              throw new DocumentFormatException(e);
            }
          } 
        
      //docId
        if (annotation.getType().matches("dc:identifier")) {
        	try {
				docId = doc.getContent().getContent(
				        annotation.getStartNode().getOffset(),
				        annotation.getEndNode().getOffset()).toString();
				
			} catch (InvalidOffsetException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
        	
        }
        //relatedDatasets
     
        if (annotation.getType().matches("dc:relation")) {
            try {
              String dataset = doc.getContent().getContent(
                annotation.getStartNode().getOffset(),
                annotation.getEndNode().getOffset()).toString();
              // add contained values as a feature to the array annotation
              if (!dataset.trim().equals("")) {
                relatedDatasets.add(dataset);
              }
            } catch (InvalidOffsetException e) {
              throw new DocumentFormatException(e);
            }
          }
        
      //dataCenter
        
        if (annotation.getType().matches("dataCenter") || annotation.getType().matches("dc:publisher")) {
            try {
             dataCenter = doc.getContent().getContent(
                annotation.getStartNode().getOffset(),
                annotation.getEndNode().getOffset()).toString();
             
            } catch (InvalidOffsetException e) {
              throw new DocumentFormatException(e);
            }
          }
       
      //dataType
        if (annotation.getType().matches("dc:type")) {
            try {
              String type = doc.getContent().getContent(
                annotation.getStartNode().getOffset(),
                annotation.getEndNode().getOffset()).toString();
              // add contained values as a feature to the array annotation
              if (!type.trim().equals("")) {
                dataTypes.add(type);
              }
            } catch (InvalidOffsetException e) {
              throw new DocumentFormatException(e);
            }
          }
        //access
        if (annotation.getType().matches("dc:rights")) {
            try {
             access = doc.getContent().getContent(
                annotation.getStartNode().getOffset(),
                annotation.getEndNode().getOffset()).toString();
             
            } catch (InvalidOffsetException e) {
              throw new DocumentFormatException(e);
            }
          }
        //linkage
        // TODO: can be several linkages - switch to Array! look for attribute(feature) 'multimedia' 'metadata' 'data'
        if (annotation.getType().matches("linkage")) {
            try {
             linkage = doc.getContent().getContent(
                annotation.getStartNode().getOffset(),
                annotation.getEndNode().getOffset()).toString();
             
            } catch (InvalidOffsetException e) {
              throw new DocumentFormatException(e);
            }
          }
      //northboundLatitude
        if (annotation.getType().matches("northBoundLatitude")) {
            try {
            	northBoundLatitude = doc.getContent().getContent(
                annotation.getStartNode().getOffset(),
                annotation.getEndNode().getOffset()).toString();
             
            } catch (InvalidOffsetException e) {
              throw new DocumentFormatException(e);
            }
          }
      //southboundLatitude
        if (annotation.getType().matches("southBoundLatitude")) {
            try {
            	southBoundLatitude = doc.getContent().getContent(
                annotation.getStartNode().getOffset(),
                annotation.getEndNode().getOffset()).toString();
             
            } catch (InvalidOffsetException e) {
              throw new DocumentFormatException(e);
            }
          }
      //eastBoundLongitude
        if (annotation.getType().matches("eastBoundLongitude")) {
            try {
            	eastBoundLongitude = doc.getContent().getContent(
                annotation.getStartNode().getOffset(),
                annotation.getEndNode().getOffset()).toString();
             
            } catch (InvalidOffsetException e) {
              throw new DocumentFormatException(e);
            }
          }
      //westboundLongitude
        if (annotation.getType().matches("westBoundLongitude")) {
            try {
            	westBoundLongitude = doc.getContent().getContent(
                annotation.getStartNode().getOffset(),
                annotation.getEndNode().getOffset()).toString();
             
            } catch (InvalidOffsetException e) {
              throw new DocumentFormatException(e);
            }
          }
      //additionalContent
        if (annotation.getType().matches("additionalContent")) {
            try {
            	additionalContent = doc.getContent().getContent(
                annotation.getStartNode().getOffset(),
                annotation.getEndNode().getOffset()).toString();
             
            } catch (InvalidOffsetException e) {
              throw new DocumentFormatException(e);
            }
          }
        
      }
    
    
   
    doc.getFeatures().put("title", title);
    doc.getFeatures().put("citation", citation);
    doc.getFeatures().put("description", description);
    doc.getFeatures().put("docId", docId);
    //DOI
    doc.getFeatures().put("dataCenter", dataCenter);
    doc.getFeatures().put("taxon", taxons.toString());
    doc.getFeatures().put("parameters", parameters.toString());
    //coordinates
    doc.getFeatures().put("minLongitude", eastBoundLongitude);
    doc.getFeatures().put("maxLongitude", westBoundLongitude);
    doc.getFeatures().put("minLatitude", northBoundLatitude);
    doc.getFeatures().put("maxLatitude", southBoundLatitude);
    
    doc.getFeatures().put("dataType", dataTypes.toString());
    //method
    //license
    doc.getFeatures().put("access", access); 
    
    doc.getFeatures().put("collectionStartDate", collectionStartDate);
    doc.getFeatures().put("collectionEndDate", collectionEndDate);
    doc.getFeatures().put("publicationDate", publicationDate);
    
    //multimedia
    doc.getFeatures().put("author", authors.toString());
    doc.getFeatures().put("contributor", contributors.toString());
    doc.getFeatures().put("keywords", keywords.toString());
    doc.getFeatures().put("relatedDatasets", relatedDatasets.toString());
    
    doc.getFeatures().put("linkage", linkage);
    doc.getFeatures().put("additionalContent", additionalContent);
     
  }

  @Override
  public Resource init() throws ResourceInstantiationException {
    // Register XML mime type
    MimeType mime = new MimeType("text", "gfbio+xml");
    // Register the class handler for this mime type
    mimeString2ClassHandlerMap.put(mime.getType() + "/" + mime.getSubtype(),
      this);
    // Register the mime type with mine string
    mimeString2mimeTypeMap.put(mime.getType() + "/" + mime.getSubtype(), mime);
    // Register file suffixes for this mime type
    suffixes2mimeTypeMap.put("xml", mime);
    // Register magic numbers for this mime type
    magic2mimeTypeMap.put("<?xml",mime);
    // Set the mimeType for this language resource
    setMimeType(mime);
    return this;
  }

}
