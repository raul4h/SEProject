#############################################################################
# Generated by PAGE version 4.11
# in conjunction with Tcl version 8.6
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(active_menu_fg) #000000
}

#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top37
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top37
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    set site_3_0 $base.fra51
    set site_3_0 $base.fra52
    set site_4_0 $site_3_0.fra40
    set site_3_0 $base.fra53
    set site_4_0 $site_3_0.fra55
    set site_4_0 $site_3_0.fra56
    set site_4_0 $site_3_0.fra57
    set site_4_0 $site_3_0.fra58
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top37 {base} {
    if {$base == ""} {
        set base .top37
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m50" -background {#ffffff} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm withdraw $top
    wm focusmodel $top passive
    wm geometry $top 942x519+314+124
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1370 749
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    label $top.lab38 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font {none 16 bold} -foreground {#FF6600} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Protocol Dissector Generator System} 
    button $top.but41 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command create_window \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -relief groove -text {Create Project} 
    vTcl:DefineAlias "$top.but41" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but42 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -relief groove -text {Close Project} 
    vTcl:DefineAlias "$top.but42" "Button2" vTcl:WidgetProc "Toplevel1" 1
    button $top.but43 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command export -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -relief groove -text {Export Project} 
    vTcl:DefineAlias "$top.but43" "Button3" vTcl:WidgetProc "Toplevel1" 1
    button $top.but44 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command dissectorScript \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -relief groove -text {Generate Dissector Script} 
    vTcl:DefineAlias "$top.but44" "Button4" vTcl:WidgetProc "Toplevel1" 1
    button $top.but45 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command organize_views \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -relief groove -text {Organize Views} 
    vTcl:DefineAlias "$top.but45" "Button5" vTcl:WidgetProc "Toplevel1" 1
    button $top.but46 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command launcher_window \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -relief groove -text {Switch Workspace} 
    vTcl:DefineAlias "$top.but46" "Button6" vTcl:WidgetProc "Toplevel1" 1
    button $top.but47 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command project_import \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -relief groove -text {Import Project} 
    vTcl:DefineAlias "$top.but47" "Button7" vTcl:WidgetProc "Toplevel1" 1
    button $top.but48 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -relief groove -text {Save Project} 
    vTcl:DefineAlias "$top.but48" "Button8" vTcl:WidgetProc "Toplevel1" 1
    button $top.but49 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command vp_start -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -relief groove -text {Open PCAP} 
    vTcl:DefineAlias "$top.but49" "Button9" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.m50
    menu $site_3_0 \
        -activebackground {#d8d8d8} -activeforeground {#ffffff} \
        -background {#d9d9d9} -font TkMenuFont -foreground {#ffffff} \
        -tearoff 0 
    frame $top.fra51 \
        -borderwidth 2 -relief groove -background {#d9d9d9} -height 455 \
        -highlightbackground {#d9d9d9} -highlightcolor black -width 175 
    vTcl:DefineAlias "$top.fra51" "Frame2" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra51
    label $site_3_0.lab38 \
        -background {#C0D5E7} -disabledforeground {#a3a3a3} \
        -font {none 12 bold} -foreground {#000000} -text {Project Navigator} 
    vTcl:DefineAlias "$site_3_0.lab38" "Label1" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TSizegrip -background #d9d9d9
    vTcl::widgets::ttk::sizegrip::CreateCmd $site_3_0.tSi46 \
        -cursor size_nw_se 
    vTcl:DefineAlias "$site_3_0.tSi46" "TSizegrip2" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab38 \
        -in $site_3_0 -x 3 -y 3 -width 168 -relwidth 0 -height 41 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tSi46 \
        -in $site_3_0 -x 80 -relx 1 -y 270 -rely 1 -anchor se \
        -bordermode inside 
    frame $top.fra52 \
        -borderwidth 2 -relief groove -background {#d9d9d9} -height 335 \
        -highlightbackground {#d9d9d9} -highlightcolor black -width 755 
    vTcl:DefineAlias "$top.fra52" "Frame3" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra52
    label $site_3_0.lab39 \
        -background {#C0D5E7} -disabledforeground {#a3a3a3} \
        -font {none 12 bold} -foreground {#000000} \
        -text {Dissector Builder Area} -width 745 
    vTcl:DefineAlias "$site_3_0.lab39" "Label2" vTcl:WidgetProc "Toplevel1" 1
    frame $site_3_0.fra40 \
        -borderwidth 2 -relief groove -background {#d9d9d9} -height 285 \
        -width 195 
    vTcl:DefineAlias "$site_3_0.fra40" "Frame5" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.fra40
    label $site_4_0.lab41 \
        -background {#C0D5E7} -disabledforeground {#a3a3a3} \
        -font {none 12 bold} -foreground {#000000} -text Palette 
    vTcl:DefineAlias "$site_4_0.lab41" "Label3" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.lab41 \
        -in $site_4_0 -x 0 -y 1 -width 194 -relwidth 0 -height 31 \
        -relheight 0 -anchor nw -bordermode ignore 
    ttk::style configure TSizegrip -background #d9d9d9
    vTcl::widgets::ttk::sizegrip::CreateCmd $site_3_0.tSi43 \
        -cursor size_nw_se 
    vTcl:DefineAlias "$site_3_0.tSi43" "TSizegrip1" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab39 \
        -in $site_3_0 -x 0 -y 0 -width 754 -relwidth 0 -height 41 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.fra40 \
        -in $site_3_0 -x 560 -y 40 -width 195 -relwidth 0 -height 285 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tSi43 \
        -in $site_3_0 -x 460 -relx 1 -y 240 -rely 1 -anchor se \
        -bordermode inside 
    frame $top.fra53 \
        -borderwidth 2 -relief groove -background {#d9d9d9} -height 115 \
        -highlightbackground {#d9d9d9} -highlightcolor black -width 755 
    vTcl:DefineAlias "$top.fra53" "Frame4" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra53
    ttk::style configure TSizegrip -background #d9d9d9
    vTcl::widgets::ttk::sizegrip::CreateCmd $site_3_0.tSi47 \
        -cursor size_nw_se 
    vTcl:DefineAlias "$site_3_0.tSi47" "TSizegrip3" vTcl:WidgetProc "Toplevel1" 1
    frame $site_3_0.fra55 \
        -borderwidth 2 -relief groove -background {#d9d9d9} -height 115 \
        -width 175 
    vTcl:DefineAlias "$site_3_0.fra55" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.fra55
    label $site_4_0.lab59 \
        -background {#C0D5E7} -disabledforeground {#a3a3a3} \
        -font {none 10 bold} -foreground {#ffffff} -text {Packet Stream Area} 
    vTcl:DefineAlias "$site_4_0.lab59" "Label4" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.lab59 \
        -in $site_4_0 -x 0 -y 1 -width 174 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    frame $site_3_0.fra56 \
        -borderwidth 2 -relief groove -background {#d9d9d9} -height 115 \
        -width 195 
    vTcl:DefineAlias "$site_3_0.fra56" "Frame6" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.fra56
    label $site_4_0.lab60 \
        -background {#C0D5E7} -disabledforeground {#a3a3a3} \
        -font {none 10 bold} -foreground {#ffffff} \
        -text {Dissected Stream Area} 
    vTcl:DefineAlias "$site_4_0.lab60" "Label5" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.lab60 \
        -in $site_4_0 -x 0 -y 1 -width 194 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    frame $site_3_0.fra57 \
        -borderwidth 2 -relief groove -background {#d9d9d9} -height 115 \
        -width 195 
    vTcl:DefineAlias "$site_3_0.fra57" "Frame7" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.fra57
    label $site_4_0.lab61 \
        -background {#C0D5E7} -disabledforeground {#a3a3a3} \
        -font {none 10 bold} -foreground {#000000} -text {Raw Data Area} 
    vTcl:DefineAlias "$site_4_0.lab61" "Label6" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.lab61 \
        -in $site_4_0 -x 0 -y 1 -width 191 -relwidth 0 -height 22 \
        -relheight 0 -anchor nw -bordermode ignore 
    frame $site_3_0.fra58 \
        -borderwidth 2 -relief groove -background {#d9d9d9} -height 115 \
        -width 195 
    vTcl:DefineAlias "$site_3_0.fra58" "Frame8" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.fra58
    label $site_4_0.lab62 \
        -background {#C0D5E7} -disabledforeground {#a3a3a3} \
        -font {none 10 bold} -foreground {#ffffff} -text {Console Area} 
    vTcl:DefineAlias "$site_4_0.lab62" "Label7" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.lab62 \
        -in $site_4_0 -x 0 -y 1 -width 191 -relwidth 0 -height 22 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tSi47 \
        -in $site_3_0 -x 730 -relx 1 -y 90 -rely 1 -anchor se \
        -bordermode inside 
    place $site_3_0.fra55 \
        -in $site_3_0 -x 0 -y 0 -width 175 -relwidth 0 -height 115 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.fra56 \
        -in $site_3_0 -x 174 -y 0 -width 195 -relwidth 0 -height 115 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.fra57 \
        -in $site_3_0 -x 368 -y 0 -width 195 -relwidth 0 -height 115 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.fra58 \
        -in $site_3_0 -x 560 -y 0 -width 195 -relwidth 0 -height 115 \
        -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab38 \
        -in $top -x 0 -y 0 -width 384 -relwidth 0 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but41 \
        -in $top -x 0 -y 30 -anchor nw -bordermode ignore 
    place $top.but42 \
        -in $top -x 190 -y 30 -anchor nw -bordermode ignore 
    place $top.but43 \
        -in $top -x 500 -y 30 -anchor nw -bordermode ignore 
    place $top.but44 \
        -in $top -x 600 -y 30 -anchor nw -bordermode ignore 
    place $top.but45 \
        -in $top -x 750 -y 30 -anchor nw -bordermode ignore 
    place $top.but46 \
        -in $top -x 280 -y 30 -anchor nw -bordermode ignore 
    place $top.but47 \
        -in $top -x 400 -y 30 -anchor nw -bordermode ignore 
    place $top.but48 \
        -in $top -x 100 -y 30 -anchor nw -bordermode ignore 
    place $top.but49 \
        -in $top -x 850 -y 30 -anchor nw -bordermode ignore 
    place $top.fra51 \
        -in $top -x 0 -y 60 -width 175 -relwidth 0 -height 455 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.fra52 \
        -in $top -x 180 -y 60 -width 755 -relwidth 0 -height 335 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.fra53 \
        -in $top -x 180 -y 400 -width 755 -relwidth 0 -height 115 \
        -relheight 0 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top37 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}
