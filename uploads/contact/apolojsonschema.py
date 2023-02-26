Apolo_Json_Schema = {
            
    "required": ["type", "namespace", "target", "variants", "chain"],
            
    "properties":{
                  
        "type":{
            "enum": ["ask", "merge"],
            "description":"'type' must be 'ask' or 'merge' and is required"
        },
                    
        "namespace":{
            "type":"string",
            "description":"'namespace' must be a string and is required"
        },
                    
        "target":{
            "type":"string",
            "description":"'target' must be a string and is required"
        },
                    
        "variants":{
            
            "type": "document",
            
            "property":{
                
                "dayOfTheWeek":{
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 7,
                    "description": "'dayOfTheWeek' must be a integer in [1, 7] and is required"
                },
            
                "day":{
                    "type": "integer",
                    "minimum": 20000101,
                    "maximum": 30001231,
                    "description": "'day' must be a integer with the format yyyymmdd and is required"
                },
            
                "month":{
                    "type": "integer",
                    "minimum": 200001,
                    "maximum": 300012,
                    "description": "'month' must be a integer with the format yyyymm and is required"
                },
            
                "year":{
                    "type": "integer",
                    "minimum": 2000,
                    "maximum": 3000,
                    "description": "'year' must be a integer with the format yyyy and is required"
                },
            }
        },
        
        "chain":{
            "type": "string",
            "description": "'chain' must be a string and is required"
        },
        
        "related":{
            
            "type": "document",
            "description": "'related' must be a document and is optional",
            
            "property":{
                
                "gender":{
                    "type": "string",
                    "enum": ["M", "F", "Otros"],
                },
            
                "city":{
                    "type": "string",
                },
            }
        },
    }
}