===================================
===================================
 BSPViewer BY: RYAN "NEMESIS" GREGG
===================================
===================================

===========================
Program/Author Information:
===========================

---- General Program Information ----
Date                     : April 14th, 2006
Author                   : Ryan "NEMESIS" Gregg
Title                    : BSPViewer
Build                    : 1.5.6
Email address            : ryansgregg@hotmail.com
Home page /  Website     : http://nemesis.thewavelength.net/

---- Program Construction Information ----
Written In               : C++ .NET

=============
Requirements:
=============

  OS
  - Windows XP
  - Windows 2000
  - Windows ME
  - Windows 98
  - Windows NT
  - Windows Server 2003

  CPU
  - 133 MHz Intel Pentium Class Processor or Equivalent (450 MHz recommended.)

  RAM
  - 64 MB of RAM (128 MB recommended.)

  GPU
  - 16 MB of RAM (64 MB recommended.)
  - 2 Texture Units

====
FAQ:
====

Q.
  When I launch BSP Viewer I get the following error message:
  "The application failed to initialize properly (0xc0000135). Click ok
  to terminate the application."

A.
  BSP Viewer is written in C++ .NET and such as requires the .NET runtimes
  to run. See the following link for more information:
  http://www.microsoft.com/downloads/details.aspx?FamilyId=262D25E3-F589-4842-8157-034D1E7CF3A3&displaylang=en


Q.

  When I launch BSP Viewer I get the following error message:
  "A required .DLL file, MSCOREE.DLL, was not found."

A.
  BSP Viewer is written in C++ .NET and such as requires the .NET runtimes
  to run. See the following link for more information:
  http://www.microsoft.com/downloads/details.aspx?FamilyId=262D25E3-F589-4842-8157-034D1E7CF3A3&displaylang=en


Q.
  How do I set BSP Viewer up?

A.
  
  To set BSP Viewer up:

   1. Go to the 'Options' menu and select 'Setup'.
   2. In the 'MOD' field enter the name of the MOD you want to use BSP Viewer
      for (valve, cstrike, dod, ns, etc.).
   3. In the 'User Path' field select your Steam user path
      (Steam\SteamApps\you@yourhost.com).
   4. Add all the packages your MOD uses (half-life.gcf should always be added).

==================
Program Changelog:
==================

  v1.5.5
  - Fixed .map exportation.

  v1.5.5
  - Fixed entity occlusion culling.
  - Improved lightmap generation.
  - Upgraded to HLLib v1.1.8.

  v1.5.4
  - Added additional info to log.
  - Fixed .wad log output.

  v1.5.3
  - Fixed .wad resource location bug.
  - Upgraded to HLLib v1.1.6.

  v1.5.2
  - Fixed crash on BSP load fail.

  v1.5.1
  - Fixed entity rendermode parsing.
  - Fixed crash caused by bad surface extents calculation.

  v1.5.0
  - Added log.
  - Added ability to edit entities in real time.
  - Added ability to export ENT files.
  - Added ability to reload packages.
  - Added File Mapping and Volatile Access package options.
  - Fixed runtime crash caused by special case faces.
  - Fixed error loading PTS error message.
  - Optimized entity occlusion culling.
  - Upgraded to HLLib v1.1.3.
  - Updated Nem's Tools link.

  v1.4.0
  - Added a package browser.
  - Added an entity browser.
  - Added the ability to select a bsp model.
  - Added the ability to mouse pick a bsp model.
  - Added ability to export 3DS files.
  - Added ability to export MAP files.
  - Added 'special entity' list.
  - Fixed origin entities.
  - Improved memory usage.
  - Improved texture exportation options.
  - Fixed garbage collection bug.

  v1.3.0
  - Added support for packages through HLLib.
  - Added skybox.

  v1.2.3
  - Added support for video cards without multitexturing.

  v1.2.2
  - Optimized entity occlusion culling.

  v1.2.1
  - Improved error messages.
  - Improved XSI UV coordinates.

  v1.2.0
  - Added ability to export XSI files.
  - Added ability to export used textures as BMP files.
  - Added ability to load PTS files.
  - Added ability to load BSP files without VIS or RAD information.
  - Improved entity occlusion culling.
  - Added ability to shell execute files.
  - Fixed camera movement.

  v1.1.1
  - Added ability to freeze culled and sorted polygons.
  - Fixed random solid colors (they were all black).

  v1.1.0
  - Transparent entity rendering and sorting added.
  - Profiler added.
  - If point used to occlusion cull entity from VIS is outside the world the
    entity is drawn all the time (instead of never).
  - Can copy camera info to clipboard.

  v1.0.1
  - When not using textures or lightmaps polys are draw in a random solid color.

==============================
Program Copyright-Permissions:
==============================

LICENSE 

Terms and Conditions for Copying, Distributing, and Modifying 

Items other than copying, distributing, and modifying the Content
with which this license was distributed (such as using, etc.) are
outside the scope of this license. 

1. You may copy and distribute exact replicas of BSPViewer as you receive
   it, in any medium, provided that you conspicuously and appropriately
   publish on each copy an appropriate copyright notice and disclaimer
   of warranty; keep intact all the notices that refer to this License
   and to the absence of any warranty; and give any other recipients of
   BSPViewer a copy of this License along with BSPViewer. You may at your
   option charge a fee for the media and/or handling involved in creating
   a unique copy of the BSPViewer for use offline, you may at your option offer
   instructional support for the BSPViewer in exchange for a fee, or you may at
   your option offer warranty in exchange for a fee. You may not charge a
   fee for BSPViewer itself. You may not charge a fee for the sole service
   of providing access to and/or use of BSPViewer via a network (e.g. the Internet),
   whether it be via the world wide web, FTP, or any other method. 

2. You may not modify your copy or copies of BSPViewer or any portion of it.

3. You are not required to accept this License, since you have not signed it.
   However, nothing else grants you permission to copy, distribute or modify BSPViewer.
   These actions are prohibited by law if you do not accept this License. Therefore,
   by copying or distributing BSPViewer you indicate your acceptance of this License to do
   so, and all its terms and conditions for copying, distributing and modifying BSPViewer. 

NO WARRANTY 

4. BECAUSE BSPVIEWER IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY
   FOR BSPVIEWER, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED
   IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE BSPVIEWER "AS IS" WITHOUT
   WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
   THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE
   ENTIRE RISK OF USE OF THE BSPVIEWER IS WITH YOU. SHOULD BSPVIEWER PROVE FAULTY, INACCURATE, OR
   OTHERWISE UNACCEPTABLE YOU ASSUME THE COST OF ALL NECESSARY REPAIR OR CORRECTION. 

5. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY
   COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MIRROR AND/OR REDISTRIBUTE BSPVIEWER AS
   PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL,
   INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE BSPVIEWER,
   EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. 