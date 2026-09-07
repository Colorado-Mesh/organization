# Colorado Mesh MeshCore Scopes

```
*                               Flood / any (default scope)
us                              Entire United States
└── west                        Western United States (+ Canada)
    └── mnw                     Mountain West (CO, UT, WY, MT, ID, NV)
        └── co                  State of Colorado

                [GEOGRAPHIC ZONES]

            └── co-ws           Western Slopes geographic zone
            └── co-fr           Front Range geographic zone
            └── co-ep           Eastern Plains geographic zone
            └── co-cm           Central Mountains geographic zone
            └── co-sl           San Luis Valley geographic zone
            
                [IATA / COLORADO MESH REGIONAL ZONES]
                
            └── co-ase          ASE IATA code / Aspen
            └── co-cos          COS IATA code / Colorado Springs
            └── co-cez          CEZ IATA code / Cortez
            └── co-den          DEN IATA code / Denver Metro
            └── co-dro          DRO IATA code / Durango
            └── co-ege          EGE IATA code / Eagle, Vail, Breckenridge
            └── co-gjt          GJT IATA code / Grand Junction
            └── co-guc          GUC IATA code / Gunnison, Crested Butte
            └── co-mtj          MTJ IATA code / Montrose
            └── co-fnl          FNL IATA code / Fort Collins, Loveland, Greeley
            └── co-pub          PUB IATA code / Pueblo
            └── co-als          ALS IATA code / San Luis Valley, Alamosa
            └── co-laa          LAA IATA code / Lamar, La Junta
            └── co-stk          STK IATA code / Sterling, Julesburg
            └── co-tex          TEX IATA code / Telluride, Ouray, Ridgway
            └── co-hdn          HDN IATA code / Yampa Valley, Hayden, Craig

                [BESPOKE / CUSTOM LOCAL SCOPES]

                ...
                
--------------------------------------------------------------------------------

            [ADDITIONAL HIERARCHY EXAMPLES, NOT RELEVANT TO COLORADO MESH]
                
        └── ut                  State of Utah
        └── wy                  State of Wyoming
            ...
        
    └── mid                     Midwest (ND, SD, NE, KS, OK, TX)
        └── ne                  State of Nebraska
            ...
        ...
    
└── east                        Eastern United States (+ Canada)
    ...   
ca                              Canada
mx                              Mexico
... 
```

Colorado Mesh recommends a hierarchical layout plan for scopes for the MeshCore network. This plan's benefits include:
- Easy-to-read ordering: Each scope is a subset of another higher-level scope. `co-XX` (two characters) signifies a geographic scope, while `co-xxx` (three characters) signifies an IATA-based scope.
- Scalable: Additional scopes can be added at any level, or a given scope can be subdivided into further sub-scopes as needed.
- Rooted in existing systems: The two primary scope categories for Colorado are driven existing airport data (IATA codes) and geographic zones as defined by the Colorado Department of Local Affairs.
- Familiar and compatible: The 16 IATA codes in Colorado have already been firmly established on the Colorado Mesh MeshCore network, including in its recommended naming scheme, and is already associated with repeater names and MeshMapper wardriving.
- High-level: Colorado Mesh does not want to overcomplicate the scopes, and instead recommends scopes that are likely to be used. The system does, however, allow for network users to introduce their own scopes and sub-scopes as they see fit (e.g. local-level)
- Non-interfering: The recommended scopes and associated zones are specific, yet broad enough to successfully limit unnecessary long-distance (cross-state or interstate) traffic without negatively impacting local area traffic.

Colorado Mesh is primarily concerned about the `co` scope and its sub-scopes, although this design is scalable and applicable for use in other states as well. Most importantly, it cooperates with the state-wide `xx` alpha2 state codes utilized by most other MeshCore networks in various U.S. states.

Colorado Mesh does/will soon provide tools and documentation to make it easy for repeater owners to apply the relevant scopes to their devices. Additional documentation has/will soon be generated to inform companion node users how to set a region scope on their traffic.