# Colorado Mesh MeshCore Scopes

```
*                               Flood / any (default scope)
us                              Entire United States
└── west                        Western United States (+ Canada)
    └── co                      State of Colorado

            [GEOGRAPHIC ZONES]

        └── co-ws               Western Slope geographic zone
        └── co-fr               Front Range geographic zone
        └── co-ep               Eastern Plains geographic zone
        └── co-cm               Central Mountains geographic zone
        └── co-sl               San Luis Valley geographic zone
            
            [IATA / COLORADO MESH REGIONAL ZONES]
                
        └── iata-ase              ASE IATA code / Aspen
        └── iata-cos              COS IATA code / Colorado Springs
        └── iata-cez              CEZ IATA code / Cortez
        └── iata-den              DEN IATA code / Denver Metro
        └── iata-dro              DRO IATA code / Durango
        └── iata-ege              EGE IATA code / Eagle, Vail, Breckenridge
        └── iata-gjt              GJT IATA code / Grand Junction
        └── iata-guc              GUC IATA code / Gunnison, Crested Butte
        └── iata-mtj              MTJ IATA code / Montrose
        └── iata-fnl              FNL IATA code / Fort Collins, Loveland, Greeley
        └── iata-pub              PUB IATA code / Pueblo
        └── iata-als              ALS IATA code / San Luis Valley, Alamosa
        └── iata-laa              LAA IATA code / Lamar, La Junta
        └── iata-stk              STK IATA code / Sterling, Julesburg
        └── iata-tex              TEX IATA code / Telluride, Ouray, Ridgway
        └── iata-hdn              HDN IATA code / Yampa Valley, Hayden, Craig
        
            [U.S. NATIONAL GRID 100^2 KM CODE]
            
            ...

            [BESPOKE / CUSTOM LOCAL SCOPES]

            ...
                
--------------------------------------------------------------------------------

[RECOMMENDED ADDITIONAL SCOPES FOR INTER-STATE COMPATIBILITY]

imw - Allows traffic to/from Utah, Idaho, Nevada
ne - Allows traffic to/from Nebraska

```

Colorado Mesh recommends a hierarchical layout plan for scopes for the MeshCore network. This plan's benefits include:
- Easy-to-read ordering: Each scope is a subset of another higher-level scope. `co-XX` (two characters) signifies a geographic scope, while `co-xxx` (three characters) signifies an IATA-based scope.
- Scalable: Additional scopes can be added at any level, or a given scope can be subdivided into further sub-scopes as needed.
- Rooted in existing systems: The two primary scope categories for Colorado are existing airport regions (IATA codes) and colloquial geographic zones recognized by state agencies.
- Supportive to emergency services: Each repeater would have the primary and eight immediately-neighboring U.S. National Grid codes as scopes, supporting a standard used by emergency services such as FEMA and search-and-rescue.
- Familiar and compatible: The 16 IATA codes in Colorado have already been firmly established on the Colorado Mesh MeshCore network, including in its recommended naming scheme, and is already associated with repeater names and MeshMapper wardriving.
- High-level: Colorado Mesh does not want to overcomplicate the scopes, and instead recommends scopes that are likely to be used. The system does, however, allow for network users to introduce their own scopes and sub-scopes as they see fit (e.g. local-level)
- Non-interfering: The recommended scopes and associated zones are specific, yet broad enough to successfully limit unnecessary long-distance (cross-state or interstate) traffic without negatively impacting local area traffic.

Colorado Mesh is primarily concerned about the `co` scope and its sub-scopes, although this design is scalable and applicable for use in other states as well.

Colorado Mesh does/will soon provide tools and documentation to make it easy for repeater owners to apply the relevant scopes to their devices. Additional documentation has/will soon be generated to inform companion node users how to set a region scope on their traffic.


## Appendix

### Intermountain West (`imw`) Scope

The `imw` scope is an established scope used by Utah, Idaho and Nevada as a top-level scope. All parts of Colorado west of the Front Range are considered part of the Intermountain West, and any repeaters in that area should carry the `imw` scope to be included in that region for relevant traffic.

### Nebraska (`ne`) Scope

Repeaters on the Colorado/Nebraska border (in the `STK` IATA region) should carry the `ne` scope as a courtesy to assist in routing neighboring Nebraska-bound traffic.

It is anticipated this same courtesy may be extended to other bordering states (Wyoming, Kansas, New Mexico) if applicable in the future.

### U.S. National Grid Scope

Each repeater, based on its latitude/longitude, belongs to one of the 100 square kilometer (~62 square mile) grid squares as defined by the U.S. National Grid system, represented by a five-character code (e.g. `13SDD` reaches from downtown Denver in the northeast to Buena Vista in the southwest).

Each repeater should carry not only the five-character code of the grid square containing it, but also its immediate eight neighbors (forming a perimeter around its containing grid square).

For example, a repeater in Bailey (zone `13SDD`) would carry the following scopes:
  - `13SDD` (primary)
    (clockwise from due north)
  - `13SDE` 
  - `13SEE`
  - `13SED`
  - `13SEC`
  - `13SDC`
  - `13SCC`
  - `13SCD`
  - `13SCE`

This allows for overlap between zone borders, allowing messages to hope into adjacent grid squares. A message sent with any U.S. National Grid system scope could therefore reach a 300 square kilometer (~186 square mile) area.

Refer to https://mmdolbow.github.io/usng-gmap-v3/ for a visualization of every code at the 100-square-kilometer level.