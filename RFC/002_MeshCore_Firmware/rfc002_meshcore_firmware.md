# Colorado Mesh MeshCore Custom Firmware

This RFC is to put forward the idea of a new custom MeshCore firmware to handle specific features. This is meant to have heavy public comments, and will be updated accordingly.

## Definitions

- Sinkhole
  - The action of a message being silently dropped
- Allowlist/blocklist
  - A list of allowed/blocked companion public IDs and/or names
- openHop
  - Python-based repeater management software: https://openhop.dev

## Proposal

As the mesh has grown, we have seen recently more and more traffic. This is a very good thing, as it shows a wide adoption across the state. However, as with any community, growth also brings bad actors. While we have not seen any true bad actors on the mesh yet, we want to prepare for the eventuality of this happening. As such, a proposal for a custom firmware with extended features and presets might be warranted going forward.

## Proposed Names

As this is a new firmware, a suitable name is appropriate, and potential names will be added here for voting on later.

- ColoMeshCore

## Proposed Features

### Default Radio Configuration

A recent talk in the wider mesh community is the FCC 500kHz bandwidth requirements. For those who do not know, the default settings in MeshCore are not compliant with FCC regulations, and most, if not all, US-based communities are currently investigating new compliant frequencies and bandwidths. We are doing the same in Colorado, though we have not figured this out yet.

Once we settle on a specific centralized frequency, this new firmware would have those settings baked-in to the firmware, meaning no extra configuration would be required on the user's end. Frequency, bandwidth, coding rate, and spreading factor would all be pre-configured and ready to go, with just the naming having to be set up.

### Blocklists

The easiest place to stop bad actors is on the mesh layer itself. By preventing the propagation of the messages across the mesh, the bad actors can be shut down before they become a problem. This primarily is solved via sinkholing messages that come from the specific companions causing the issues via blocklists.

Currently, MeshCore does not have this as a native feature, only openHop does. There are a few forks that do this already, and we should base our new firmware on one of these forks.

#### Blocked Message Forwarding

A secondary feature of blocklists would be the ability to send the blocked messages on a specific channel for review by the admins (with that channel being private and not blocklisted). This would help with diagnosing if someone is accidentally getting sinkholed, or if appeals are being made to remove someone from the blocklist.

### Fleet Management

Another feature that may be helpful is to bake-in fleet management. This would allow users to opt-in via allowlists to let the aforementioned blocklists be managed by trusted Colorado Mesh admins mesh-wide. This would also allow users with larger fleets of repeaters to centrally manage them and make large changes all at once via a separate channel only that user knows, allowing only their companions to make changes on them.

**This feature would be fully opt-in, and fleet management can be used without opting in to the Colorado Mesh admin fleet management**

## Similar Projects

Pre-existing projects that implement some or all of the features listed above will be added below

### nightcrawler's fork

**GitHub:** https://github.com/jhuebert/MeshCore

This fork implements the majority of these features already, reducing the overhead for implementing the Colorado Mesh firmware

## Concerns

Major concerns raised by the comments will be added below

### Centralization of the Mesh

This proposal does enact some level of centralization past what already exists on the mesh. Right now, most features on the mesh are defaults or are visual only (naming schemes). However, this RFC proposes a change that centralizes a lot of management to the Colorado Mesh group, which may be divisive. Comments are appreciated on this matter
