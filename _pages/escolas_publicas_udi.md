---
layout: page
title: Mapa das Escolas Públicas de Uberlândia	
permalink: /escolas_pub_udi/
---

<div>
    <head>    
        <meta http-equiv="content-type" content="text/html; charset=UTF-8" />

            <script>
                L_NO_TOUCH = false;
                L_DISABLE_3D = false;
            </script>

        <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
        <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
        <script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js"></script>
        <script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css"/>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"/>
        <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css"/>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css"/>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css"/>

                <meta name="viewport" content="width=device-width,
                    initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
                <style>
                    #map_b6fd6ebc617c1509ca1a4ffb4cc2df85 {
                        position: relative;
                        width: 100.0%;
                        height: 100.0%;
                        left: 0.0%;
                        top: 0.0%;
                    }
                    .leaflet-container { font-size: 1rem; }
                </style>

</head>
<body>
    
    
            <div class="folium-map" id="map_b6fd6ebc617c1509ca1a4ffb4cc2df85" ></div>
        
</body>
<script>
    
    
            var map_b6fd6ebc617c1509ca1a4ffb4cc2df85 = L.map(
                "map_b6fd6ebc617c1509ca1a4ffb4cc2df85",
                {
                    center: [-18.9186, -48.2772],
                    crs: L.CRS.EPSG3857,
                    zoom: 13,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );

            

        
    
            var tile_layer_b12701a7cb92739d2e13e12566017894 = L.tileLayer(
                "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                {"attribution": "Data by \u0026copy; \u003ca target=\"_blank\" href=\"http://openstreetmap.org\"\u003eOpenStreetMap\u003c/a\u003e, under \u003ca target=\"_blank\" href=\"http://www.openstreetmap.org/copyright\"\u003eODbL\u003c/a\u003e.", "detectRetina": false, "maxNativeZoom": 18, "maxZoom": 18, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var marker_16a7f2faa8b6ead7460aaa3f9b2f3f8d = L.marker(
                [-18.9328283, -48.2800704],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_bd75185d6896729c6c43f06c14057b89 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_16a7f2faa8b6ead7460aaa3f9b2f3f8d.setIcon(icon_bd75185d6896729c6c43f06c14057b89);
        
    
        var popup_071f50325e384bda4a4332836449bdb5 = L.popup({"maxWidth": "100%"});

        
            
                var html_db393a9fcab42002948e4c1c008c0bd9 = $(`<div id="html_db393a9fcab42002948e4c1c008c0bd9" style="width: 100.0%; height: 100.0%;">IFTM - CAMPUS UBERLANDIA CENTRO---</div>`)[0];
                popup_071f50325e384bda4a4332836449bdb5.setContent(html_db393a9fcab42002948e4c1c008c0bd9);
            
        

        marker_16a7f2faa8b6ead7460aaa3f9b2f3f8d.bindPopup(popup_071f50325e384bda4a4332836449bdb5)
        ;

        
    
    
            var marker_7b682fb8cbafd68ba283b4470f269d44 = L.marker(
                [-18.9078203, -48.2623873],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_ceecbb62ac9533c3e418f082475e791d = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_7b682fb8cbafd68ba283b4470f269d44.setIcon(icon_ceecbb62ac9533c3e418f082475e791d);
        
    
        var popup_685cb3dea2a33cda8abe8dd03f32fbe9 = L.popup({"maxWidth": "100%"});

        
            
                var html_b3fd417c348a53e3c0e23a1aa63ed569 = $(`<div id="html_b3fd417c348a53e3c0e23a1aa63ed569" style="width: 100.0%; height: 100.0%;">ESCOLA DE EDUCACAO BASICA DA UFU---</div>`)[0];
                popup_685cb3dea2a33cda8abe8dd03f32fbe9.setContent(html_b3fd417c348a53e3c0e23a1aa63ed569);
            
        

        marker_7b682fb8cbafd68ba283b4470f269d44.bindPopup(popup_685cb3dea2a33cda8abe8dd03f32fbe9)
        ;

        
    
    
            var marker_f817177bdf7992455e61604574d6b36f = L.marker(
                [-18.7967317, -48.3084472],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_f85d37917a9824c9a3696832976d94c6 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_f817177bdf7992455e61604574d6b36f.setIcon(icon_f85d37917a9824c9a3696832976d94c6);
        
    
        var popup_3cd88871f64405a6314c6b7dd877d7f7 = L.popup({"maxWidth": "100%"});

        
            
                var html_58622bf75422a1637dc7aae3910f3714 = $(`<div id="html_58622bf75422a1637dc7aae3910f3714" style="width: 100.0%; height: 100.0%;">IFTM - CAMPUS UBERLANDIA---</div>`)[0];
                popup_3cd88871f64405a6314c6b7dd877d7f7.setContent(html_58622bf75422a1637dc7aae3910f3714);
            
        

        marker_f817177bdf7992455e61604574d6b36f.bindPopup(popup_3cd88871f64405a6314c6b7dd877d7f7)
        ;

        
    
    
            var marker_5957f7990289a4819472a3ad8ec745b1 = L.marker(
                [-18.9185039, -48.2581692],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_fa7c9d4f00657976fc2770fdf4bc0a97 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_5957f7990289a4819472a3ad8ec745b1.setIcon(icon_fa7c9d4f00657976fc2770fdf4bc0a97);
        
    
        var popup_35ff1a0735d376ad010ba5db2cf463ff = L.popup({"maxWidth": "100%"});

        
            
                var html_9f4b44cd2aedc94fab6f44d6eaa96a76 = $(`<div id="html_9f4b44cd2aedc94fab6f44d6eaa96a76" style="width: 100.0%; height: 100.0%;">UFU - ESCOLA TECNICA DE SAUDE---</div>`)[0];
                popup_35ff1a0735d376ad010ba5db2cf463ff.setContent(html_9f4b44cd2aedc94fab6f44d6eaa96a76);
            
        

        marker_5957f7990289a4819472a3ad8ec745b1.bindPopup(popup_35ff1a0735d376ad010ba5db2cf463ff)
        ;

        
    
    
            var marker_3280bc3417a2e8f452b1e46daf1fb620 = L.marker(
                [-18.8896352, -48.2678753],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_4bf4096d0c558c9808dc8ab1d29d6172 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_3280bc3417a2e8f452b1e46daf1fb620.setIcon(icon_4bf4096d0c558c9808dc8ab1d29d6172);
        
    
        var popup_dec8e858734806212e86d58d81ede7be = L.popup({"maxWidth": "100%"});

        
            
                var html_3d1be599a165fd101a66902361324a9b = $(`<div id="html_3d1be599a165fd101a66902361324a9b" style="width: 100.0%; height: 100.0%;">EE ENEIAS VASCONCELOS---</div>`)[0];
                popup_dec8e858734806212e86d58d81ede7be.setContent(html_3d1be599a165fd101a66902361324a9b);
            
        

        marker_3280bc3417a2e8f452b1e46daf1fb620.bindPopup(popup_dec8e858734806212e86d58d81ede7be)
        ;

        
    
    
            var marker_6487d3191f0a0191c7f439b98f5aac15 = L.marker(
                [-18.8912158, -48.2472451],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_0a42d4179016e9cab8d93e43a8289233 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_6487d3191f0a0191c7f439b98f5aac15.setIcon(icon_0a42d4179016e9cab8d93e43a8289233);
        
    
        var popup_a4e53f6b781fe10939016e6e1f2c2c15 = L.popup({"maxWidth": "100%"});

        
            
                var html_87ab89439fdf8d5dd5473ef89d419e25 = $(`<div id="html_87ab89439fdf8d5dd5473ef89d419e25" style="width: 100.0%; height: 100.0%;">EE CUSTODIO DA COSTA PEREIRA---</div>`)[0];
                popup_a4e53f6b781fe10939016e6e1f2c2c15.setContent(html_87ab89439fdf8d5dd5473ef89d419e25);
            
        

        marker_6487d3191f0a0191c7f439b98f5aac15.bindPopup(popup_a4e53f6b781fe10939016e6e1f2c2c15)
        ;

        
    
    
            var marker_d56fd9487b913c9256f378f57c826846 = L.marker(
                [-18.9816615, -48.265211],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_60eaa808146693e3515e945474ca5a3c = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_d56fd9487b913c9256f378f57c826846.setIcon(icon_60eaa808146693e3515e945474ca5a3c);
        
    
        var popup_f8e400b7f37dd06a3924a97dabe002e3 = L.popup({"maxWidth": "100%"});

        
            
                var html_50a4462f2838791851e9819a30b6d48b = $(`<div id="html_50a4462f2838791851e9819a30b6d48b" style="width: 100.0%; height: 100.0%;">EE FELISBERTO ALVES CARREJO---</div>`)[0];
                popup_f8e400b7f37dd06a3924a97dabe002e3.setContent(html_50a4462f2838791851e9819a30b6d48b);
            
        

        marker_d56fd9487b913c9256f378f57c826846.bindPopup(popup_f8e400b7f37dd06a3924a97dabe002e3)
        ;

        
    
    
            var marker_2e77a9defc0e753e2bf64b493d5f4d80 = L.marker(
                [-18.9184854, -48.2901865],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_3e139531a962f274858986a59aed2c13 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_2e77a9defc0e753e2bf64b493d5f4d80.setIcon(icon_3e139531a962f274858986a59aed2c13);
        
    
        var popup_1c67594a6674aaa68efa478493faba1c = L.popup({"maxWidth": "100%"});

        
            
                var html_137d7f03d49975368af65059eaf7fb9b = $(`<div id="html_137d7f03d49975368af65059eaf7fb9b" style="width: 100.0%; height: 100.0%;">EE AFONSO ARINOS---</div>`)[0];
                popup_1c67594a6674aaa68efa478493faba1c.setContent(html_137d7f03d49975368af65059eaf7fb9b);
            
        

        marker_2e77a9defc0e753e2bf64b493d5f4d80.bindPopup(popup_1c67594a6674aaa68efa478493faba1c)
        ;

        
    
    
            var marker_3fa8a5ba93f2f73c026dae70cde11821 = L.marker(
                [-18.8958618, -48.28400689999999],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_abd4a5102572590342648abdceb086d1 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_3fa8a5ba93f2f73c026dae70cde11821.setIcon(icon_abd4a5102572590342648abdceb086d1);
        
    
        var popup_a97bfc0f6672b78c266b3cf36e0db171 = L.popup({"maxWidth": "100%"});

        
            
                var html_b416c04890bef67b5bcbd1ce14ce79e6 = $(`<div id="html_b416c04890bef67b5bcbd1ce14ce79e6" style="width: 100.0%; height: 100.0%;">EE GUIOMAR DE FREITAS COSTA---</div>`)[0];
                popup_a97bfc0f6672b78c266b3cf36e0db171.setContent(html_b416c04890bef67b5bcbd1ce14ce79e6);
            
        

        marker_3fa8a5ba93f2f73c026dae70cde11821.bindPopup(popup_a97bfc0f6672b78c266b3cf36e0db171)
        ;

        
    
    
            var marker_d42b7b8d5454030758f92734319c89af = L.marker(
                [-18.8888761, -48.2740212],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_4575c01dafdd2f3074fdf6bc866f0bf7 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_d42b7b8d5454030758f92734319c89af.setIcon(icon_4575c01dafdd2f3074fdf6bc866f0bf7);
        
    
        var popup_99797e0ee4621dd52b41eb344776b5d0 = L.popup({"maxWidth": "100%"});

        
            
                var html_96646225a84d64538e06260be01f2913 = $(`<div id="html_96646225a84d64538e06260be01f2913" style="width: 100.0%; height: 100.0%;">EE HORTENCIO DINIZ---</div>`)[0];
                popup_99797e0ee4621dd52b41eb344776b5d0.setContent(html_96646225a84d64538e06260be01f2913);
            
        

        marker_d42b7b8d5454030758f92734319c89af.bindPopup(popup_99797e0ee4621dd52b41eb344776b5d0)
        ;

        
    
    
            var marker_e29d72d345f022a9de667d9ec6678eaa = L.marker(
                [-18.9251638, -48.2745463],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_78c2359b295cdae30ed12675d19ae0ff = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_e29d72d345f022a9de667d9ec6678eaa.setIcon(icon_78c2359b295cdae30ed12675d19ae0ff);
        
    
        var popup_be1a86fd3113383f23a3644701976f42 = L.popup({"maxWidth": "100%"});

        
            
                var html_5abf294a75d464e0052f0bd80a138257 = $(`<div id="html_5abf294a75d464e0052f0bd80a138257" style="width: 100.0%; height: 100.0%;">EE HONORIO GUIMARAES---</div>`)[0];
                popup_be1a86fd3113383f23a3644701976f42.setContent(html_5abf294a75d464e0052f0bd80a138257);
            
        

        marker_e29d72d345f022a9de667d9ec6678eaa.bindPopup(popup_be1a86fd3113383f23a3644701976f42)
        ;

        
    
    
            var marker_183637b1faa6c4c2d475c5c61b4d23eb = L.marker(
                [-18.9589958, -48.312881],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_46771b76c187b22eda22cda59bbb434b = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_183637b1faa6c4c2d475c5c61b4d23eb.setIcon(icon_46771b76c187b22eda22cda59bbb434b);
        
    
        var popup_95a20ba3b9bd236ba13d6abea0d0d55d = L.popup({"maxWidth": "100%"});

        
            
                var html_f4d15d66848812695645aeeb4a5fbbf3 = $(`<div id="html_f4d15d66848812695645aeeb4a5fbbf3" style="width: 100.0%; height: 100.0%;">EE ALDA MOTA BATISTA---</div>`)[0];
                popup_95a20ba3b9bd236ba13d6abea0d0d55d.setContent(html_f4d15d66848812695645aeeb4a5fbbf3);
            
        

        marker_183637b1faa6c4c2d475c5c61b4d23eb.bindPopup(popup_95a20ba3b9bd236ba13d6abea0d0d55d)
        ;

        
    
    
            var marker_6e64b71ea5b826f93430054984fb2826 = L.marker(
                [-18.908013, -48.284817],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_9308eee00e1c9c9e987248d4440b649c = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_6e64b71ea5b826f93430054984fb2826.setIcon(icon_9308eee00e1c9c9e987248d4440b649c);
        
    
        var popup_6a8f0473b7f931cd2087b24e8ab5e3f4 = L.popup({"maxWidth": "100%"});

        
            
                var html_887d7d1a584c4fd6dda627161f0ff82f = $(`<div id="html_887d7d1a584c4fd6dda627161f0ff82f" style="width: 100.0%; height: 100.0%;">EE IGNACIO PAES LEME---</div>`)[0];
                popup_6a8f0473b7f931cd2087b24e8ab5e3f4.setContent(html_887d7d1a584c4fd6dda627161f0ff82f);
            
        

        marker_6e64b71ea5b826f93430054984fb2826.bindPopup(popup_6a8f0473b7f931cd2087b24e8ab5e3f4)
        ;

        
    
    
            var marker_73a722897f073c605ec4c982cf5d78c2 = L.marker(
                [-18.9136661, -48.3327883],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_ca100425b3fbb8a7fd17ce3822d65608 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_73a722897f073c605ec4c982cf5d78c2.setIcon(icon_ca100425b3fbb8a7fd17ce3822d65608);
        
    
        var popup_7510cac850c3c06f10fd1dccd6a6782c = L.popup({"maxWidth": "100%"});

        
            
                var html_dca21a01ce8d3d2ffd30ea7eef093349 = $(`<div id="html_dca21a01ce8d3d2ffd30ea7eef093349" style="width: 100.0%; height: 100.0%;">EE PROFESSORA JUVENILIA FERREIRA DOS SANTOS---</div>`)[0];
                popup_7510cac850c3c06f10fd1dccd6a6782c.setContent(html_dca21a01ce8d3d2ffd30ea7eef093349);
            
        

        marker_73a722897f073c605ec4c982cf5d78c2.bindPopup(popup_7510cac850c3c06f10fd1dccd6a6782c)
        ;

        
    
    
            var marker_9defc028faaaa7ec5d669b3cd44cef6c = L.marker(
                [-18.921225, -48.2640928],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_37f8187c070ae3bf6e57f02b000b11cc = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_9defc028faaaa7ec5d669b3cd44cef6c.setIcon(icon_37f8187c070ae3bf6e57f02b000b11cc);
        
    
        var popup_fb57427e261028f23473849a637e0d41 = L.popup({"maxWidth": "100%"});

        
            
                var html_2d539e7f7ca6142220510c06fd09362c = $(`<div id="html_2d539e7f7ca6142220510c06fd09362c" style="width: 100.0%; height: 100.0%;">EE JOAQUIM SARAIVA---</div>`)[0];
                popup_fb57427e261028f23473849a637e0d41.setContent(html_2d539e7f7ca6142220510c06fd09362c);
            
        

        marker_9defc028faaaa7ec5d669b3cd44cef6c.bindPopup(popup_fb57427e261028f23473849a637e0d41)
        ;

        
    
    
            var marker_b9bf2f2fa0f0b9b410119d244d3f79da = L.marker(
                [-18.9256662, -48.28598419999999],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_bf9d3fdaf110bf36e9cd3ca761d9985a = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_b9bf2f2fa0f0b9b410119d244d3f79da.setIcon(icon_bf9d3fdaf110bf36e9cd3ca761d9985a);
        
    
        var popup_77c14de7da921eff4d0350277e70f35d = L.popup({"maxWidth": "100%"});

        
            
                var html_a7a013e06b124d45d55d3dd4c6323058 = $(`<div id="html_a7a013e06b124d45d55d3dd4c6323058" style="width: 100.0%; height: 100.0%;">EE AMERICO RENE GIANNETTI---</div>`)[0];
                popup_77c14de7da921eff4d0350277e70f35d.setContent(html_a7a013e06b124d45d55d3dd4c6323058);
            
        

        marker_b9bf2f2fa0f0b9b410119d244d3f79da.bindPopup(popup_77c14de7da921eff4d0350277e70f35d)
        ;

        
    
    
            var marker_0c2878d975f2de60dfde394a842bd484 = L.marker(
                [-18.9002692, -48.2627997],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_d269bf80b417a43bddcdaa67922f0cc8 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_0c2878d975f2de60dfde394a842bd484.setIcon(icon_d269bf80b417a43bddcdaa67922f0cc8);
        
    
        var popup_5733e9cc20c7be0833adf01353f93b8e = L.popup({"maxWidth": "100%"});

        
            
                var html_c27e5061656c1159ed912e9963978f8c = $(`<div id="html_c27e5061656c1159ed912e9963978f8c" style="width: 100.0%; height: 100.0%;">EE PROFESSOR JOSE IGNACIO DE SOUSA---</div>`)[0];
                popup_5733e9cc20c7be0833adf01353f93b8e.setContent(html_c27e5061656c1159ed912e9963978f8c);
            
        

        marker_0c2878d975f2de60dfde394a842bd484.bindPopup(popup_5733e9cc20c7be0833adf01353f93b8e)
        ;

        
    
    
            var marker_8aba5064e8fc3738d22bfd4836664d96 = L.marker(
                [-18.8681259, -48.2852644],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_9d1ea502ac182fbe9ed765c468aca04d = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_8aba5064e8fc3738d22bfd4836664d96.setIcon(icon_9d1ea502ac182fbe9ed765c468aca04d);
        
    
        var popup_5f5dd338087d8133b959ff7798e989ab = L.popup({"maxWidth": "100%"});

        
            
                var html_99b0b6d5f7caa49df514f0d32e626fc6 = $(`<div id="html_99b0b6d5f7caa49df514f0d32e626fc6" style="width: 100.0%; height: 100.0%;">EE NO CONJUNTO HABITACIONAL CRUZEIRO DO SUL---</div>`)[0];
                popup_5f5dd338087d8133b959ff7798e989ab.setContent(html_99b0b6d5f7caa49df514f0d32e626fc6);
            
        

        marker_8aba5064e8fc3738d22bfd4836664d96.bindPopup(popup_5f5dd338087d8133b959ff7798e989ab)
        ;

        
    
    
            var marker_2def8078add939530d41f74862782d62 = L.marker(
                [-18.9212774, -48.2942918],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_0aff089da90a7d82c6c11659e8172e0c = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_2def8078add939530d41f74862782d62.setIcon(icon_0aff089da90a7d82c6c11659e8172e0c);
        
    
        var popup_8175f02b5edff6486d43362d3c6d5957 = L.popup({"maxWidth": "100%"});

        
            
                var html_77dfafa965498d88462912ef15f96526 = $(`<div id="html_77dfafa965498d88462912ef15f96526" style="width: 100.0%; height: 100.0%;">EE JOSE ZACHARIAS JUNQUEIRA---</div>`)[0];
                popup_8175f02b5edff6486d43362d3c6d5957.setContent(html_77dfafa965498d88462912ef15f96526);
            
        

        marker_2def8078add939530d41f74862782d62.bindPopup(popup_8175f02b5edff6486d43362d3c6d5957)
        ;

        
    
    
            var marker_13e1ac41cc564bbf0c39443aedf93292 = L.marker(
                [-18.9104911, -48.2649971],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_2e40fd0dbc1bbeb20e86dc614d67a796 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_13e1ac41cc564bbf0c39443aedf93292.setIcon(icon_2e40fd0dbc1bbeb20e86dc614d67a796);
        
    
        var popup_8f564671cc92dfba4fb57f158b71b5f5 = L.popup({"maxWidth": "100%"});

        
            
                var html_65ef5690a22ec34f52ec09015b27bffe = $(`<div id="html_65ef5690a22ec34f52ec09015b27bffe" style="width: 100.0%; height: 100.0%;">EE AMADOR NAVES---</div>`)[0];
                popup_8f564671cc92dfba4fb57f158b71b5f5.setContent(html_65ef5690a22ec34f52ec09015b27bffe);
            
        

        marker_13e1ac41cc564bbf0c39443aedf93292.bindPopup(popup_8f564671cc92dfba4fb57f158b71b5f5)
        ;

        
    
    
            var marker_45a3a2a9dce3d4db12de05a8c490c3f7 = L.marker(
                [-18.9276465, -48.3041068],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_f1024f7a6d99c97822ebb0fd0ce749b6 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_45a3a2a9dce3d4db12de05a8c490c3f7.setIcon(icon_f1024f7a6d99c97822ebb0fd0ce749b6);
        
    
        var popup_c568e9f7b2c4d732d1d6fb3d7211e2d5 = L.popup({"maxWidth": "100%"});

        
            
                var html_017149ff57b692326803442cc2e53c48 = $(`<div id="html_017149ff57b692326803442cc2e53c48" style="width: 100.0%; height: 100.0%;">EE MARECHAL CASTELO BRANCO---</div>`)[0];
                popup_c568e9f7b2c4d732d1d6fb3d7211e2d5.setContent(html_017149ff57b692326803442cc2e53c48);
            
        

        marker_45a3a2a9dce3d4db12de05a8c490c3f7.bindPopup(popup_c568e9f7b2c4d732d1d6fb3d7211e2d5)
        ;

        
    
    
            var marker_036518520a2011ae2d08575e868eb1b0 = L.marker(
                [-18.9200005, -48.3315102],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_ab4a693d1dba6ce1f28624beae75eeb7 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_036518520a2011ae2d08575e868eb1b0.setIcon(icon_ab4a693d1dba6ce1f28624beae75eeb7);
        
    
        var popup_215efe9acada27829424fa9f5fc13384 = L.popup({"maxWidth": "100%"});

        
            
                var html_660723ded0fba0bded6b75b2561a732d = $(`<div id="html_660723ded0fba0bded6b75b2561a732d" style="width: 100.0%; height: 100.0%;">EE PROFESSOR LEONIDAS DE CASTRO SERRA---</div>`)[0];
                popup_215efe9acada27829424fa9f5fc13384.setContent(html_660723ded0fba0bded6b75b2561a732d);
            
        

        marker_036518520a2011ae2d08575e868eb1b0.bindPopup(popup_215efe9acada27829424fa9f5fc13384)
        ;

        
    
    
            var marker_873d62561e98290851690c1560b4bc75 = L.marker(
                [-18.9648525, -48.3278756],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_f59fa19092c38dbf13e3600ab55a44ee = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_873d62561e98290851690c1560b4bc75.setIcon(icon_f59fa19092c38dbf13e3600ab55a44ee);
        
    
        var popup_912579e0a56ecfe04e1f32615a99d3e2 = L.popup({"maxWidth": "100%"});

        
            
                var html_ca21e33b31022a350bf60c4ec280790b = $(`<div id="html_ca21e33b31022a350bf60c4ec280790b" style="width: 100.0%; height: 100.0%;">EE MARIO PORTO---</div>`)[0];
                popup_912579e0a56ecfe04e1f32615a99d3e2.setContent(html_ca21e33b31022a350bf60c4ec280790b);
            
        

        marker_873d62561e98290851690c1560b4bc75.bindPopup(popup_912579e0a56ecfe04e1f32615a99d3e2)
        ;

        
    
    
            var marker_f1cc3ca4d81bcdaeb2dc4eaf7f3c2aee = L.marker(
                [-18.9187974, -48.2946226],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_1d1299a8702ad01d97b6af3c2041ae32 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_f1cc3ca4d81bcdaeb2dc4eaf7f3c2aee.setIcon(icon_1d1299a8702ad01d97b6af3c2041ae32);
        
    
        var popup_fefe10e67bce4d39dad479c4329cc143 = L.popup({"maxWidth": "100%"});

        
            
                var html_77428858701ba6f825836c81d07ba66c = $(`<div id="html_77428858701ba6f825836c81d07ba66c" style="width: 100.0%; height: 100.0%;">EE ANGELA TEIXEIRA DA SILVA---</div>`)[0];
                popup_fefe10e67bce4d39dad479c4329cc143.setContent(html_77428858701ba6f825836c81d07ba66c);
            
        

        marker_f1cc3ca4d81bcdaeb2dc4eaf7f3c2aee.bindPopup(popup_fefe10e67bce4d39dad479c4329cc143)
        ;

        
    
    
            var marker_e748b2404508fb99d92bb9ca70d7c042 = L.marker(
                [-18.917315, -48.281483],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_c9e94010b909008c0df470d6b7f8fa8c = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_e748b2404508fb99d92bb9ca70d7c042.setIcon(icon_c9e94010b909008c0df470d6b7f8fa8c);
        
    
        var popup_7c4e741f2c55a6847dadb5e9949b74f3 = L.popup({"maxWidth": "100%"});

        
            
                var html_2beceeef0b5c09727b8a87c9b84908aa = $(`<div id="html_2beceeef0b5c09727b8a87c9b84908aa" style="width: 100.0%; height: 100.0%;">EE MARIA DA CONCEICAO BARBOSA DE SOUZA---</div>`)[0];
                popup_7c4e741f2c55a6847dadb5e9949b74f3.setContent(html_2beceeef0b5c09727b8a87c9b84908aa);
            
        

        marker_e748b2404508fb99d92bb9ca70d7c042.bindPopup(popup_7c4e741f2c55a6847dadb5e9949b74f3)
        ;

        
    
    
            var marker_4d383005e05f18b00b3e06ebbf9d8006 = L.marker(
                [-18.8852023, -48.28845500000001],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_a33dbc231e476e761e5f43ead102461c = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_4d383005e05f18b00b3e06ebbf9d8006.setIcon(icon_a33dbc231e476e761e5f43ead102461c);
        
    
        var popup_c48b2645718c2b779411af9a7f77d57c = L.popup({"maxWidth": "100%"});

        
            
                var html_97329c01b59f80764467fa2b80351fdd = $(`<div id="html_97329c01b59f80764467fa2b80351fdd" style="width: 100.0%; height: 100.0%;">EE PROFESSOR NELSON CUPERTINO---</div>`)[0];
                popup_c48b2645718c2b779411af9a7f77d57c.setContent(html_97329c01b59f80764467fa2b80351fdd);
            
        

        marker_4d383005e05f18b00b3e06ebbf9d8006.bindPopup(popup_c48b2645718c2b779411af9a7f77d57c)
        ;

        
    
    
            var marker_88d1ff9e51afe9f93ff77e3a639b2872 = L.marker(
                [-18.9126277, -48.2624163],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_1f46288e7a1e6a89035053384910973f = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_88d1ff9e51afe9f93ff77e3a639b2872.setIcon(icon_1f46288e7a1e6a89035053384910973f);
        
    
        var popup_eee0c22e5f6823a0b6240d6a04c7fbb8 = L.popup({"maxWidth": "100%"});

        
            
                var html_75d20bd6db4bd7f7f0895d67905c2f87 = $(`<div id="html_75d20bd6db4bd7f7f0895d67905c2f87" style="width: 100.0%; height: 100.0%;">EE MESSIAS PEDREIRO---</div>`)[0];
                popup_eee0c22e5f6823a0b6240d6a04c7fbb8.setContent(html_75d20bd6db4bd7f7f0895d67905c2f87);
            
        

        marker_88d1ff9e51afe9f93ff77e3a639b2872.bindPopup(popup_eee0c22e5f6823a0b6240d6a04c7fbb8)
        ;

        
    
    
            var marker_a09cdfb67fee2df44788ef05594736f3 = L.marker(
                [-18.9256662, -48.28598419999999],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_25f1d87a4476b4ec47322214ad197441 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_a09cdfb67fee2df44788ef05594736f3.setIcon(icon_25f1d87a4476b4ec47322214ad197441);
        
    
        var popup_f0ab72f914fd618f4a9d7066ade13d8f = L.popup({"maxWidth": "100%"});

        
            
                var html_3942b86f4ba3846fd6062a61544357de = $(`<div id="html_3942b86f4ba3846fd6062a61544357de" style="width: 100.0%; height: 100.0%;">EE ENEAS DE OLIVEIRA GUIMARAES---</div>`)[0];
                popup_f0ab72f914fd618f4a9d7066ade13d8f.setContent(html_3942b86f4ba3846fd6062a61544357de);
            
        

        marker_a09cdfb67fee2df44788ef05594736f3.bindPopup(popup_f0ab72f914fd618f4a9d7066ade13d8f)
        ;

        
    
    
            var marker_d078ce05f0028209058b29c92e7f50e4 = L.marker(
                [-18.8831644, -48.281471],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_3ac27c1b40dcdac93e92dc34521dcd01 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_d078ce05f0028209058b29c92e7f50e4.setIcon(icon_3ac27c1b40dcdac93e92dc34521dcd01);
        
    
        var popup_13437c59f70cccedfe7abf54d74473c0 = L.popup({"maxWidth": "100%"});

        
            
                var html_d12619809bc06586b9d8ab55eef2c5f6 = $(`<div id="html_d12619809bc06586b9d8ab55eef2c5f6" style="width: 100.0%; height: 100.0%;">EE ANGELINO PAVAN---</div>`)[0];
                popup_13437c59f70cccedfe7abf54d74473c0.setContent(html_d12619809bc06586b9d8ab55eef2c5f6);
            
        

        marker_d078ce05f0028209058b29c92e7f50e4.bindPopup(popup_13437c59f70cccedfe7abf54d74473c0)
        ;

        
    
    
            var marker_099a3af1f5a5d0f8d6f0b7f90b46c4e4 = L.marker(
                [-18.9120645, -48.2947004],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_1cc5a840234b90312cf485f1d1e0f61b = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_099a3af1f5a5d0f8d6f0b7f90b46c4e4.setIcon(icon_1cc5a840234b90312cf485f1d1e0f61b);
        
    
        var popup_66d938cc48663b49bd82a844e7e4b131 = L.popup({"maxWidth": "100%"});

        
            
                var html_8097d6506c6f77f896be63a8fa9c7f50 = $(`<div id="html_8097d6506c6f77f896be63a8fa9c7f50" style="width: 100.0%; height: 100.0%;">EE OSVALDO RESENDE---</div>`)[0];
                popup_66d938cc48663b49bd82a844e7e4b131.setContent(html_8097d6506c6f77f896be63a8fa9c7f50);
            
        

        marker_099a3af1f5a5d0f8d6f0b7f90b46c4e4.bindPopup(popup_66d938cc48663b49bd82a844e7e4b131)
        ;

        
    
    
            var marker_ffe38308031930158943a8216c7a4a02 = L.marker(
                [-18.9026756, -48.2712593],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_3295d7f1266eb180b328bea2bd3d0cd4 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_ffe38308031930158943a8216c7a4a02.setIcon(icon_3295d7f1266eb180b328bea2bd3d0cd4);
        
    
        var popup_424d685a715159600ebe22108e824039 = L.popup({"maxWidth": "100%"});

        
            
                var html_cd152e37373db320716c96c5f75a6675 = $(`<div id="html_cd152e37373db320716c96c5f75a6675" style="width: 100.0%; height: 100.0%;">EE ANTONIO LUIS BASTOS---</div>`)[0];
                popup_424d685a715159600ebe22108e824039.setContent(html_cd152e37373db320716c96c5f75a6675);
            
        

        marker_ffe38308031930158943a8216c7a4a02.bindPopup(popup_424d685a715159600ebe22108e824039)
        ;

        
    
    
            var marker_bdfb9c34132cd5f3452a74b3cb52ad1f = L.marker(
                [-18.8974408, -48.2815488],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_e7d63d3b3912c4bd6b9257111579f7c5 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_bdfb9c34132cd5f3452a74b3cb52ad1f.setIcon(icon_e7d63d3b3912c4bd6b9257111579f7c5);
        
    
        var popup_7fb2edff3c7b86444954c7d989baf7cf = L.popup({"maxWidth": "100%"});

        
            
                var html_32e669407c8f46ec2ae4b9924f58eca4 = $(`<div id="html_32e669407c8f46ec2ae4b9924f58eca4" style="width: 100.0%; height: 100.0%;">EE PADRE MARIO FORESTAN---</div>`)[0];
                popup_7fb2edff3c7b86444954c7d989baf7cf.setContent(html_32e669407c8f46ec2ae4b9924f58eca4);
            
        

        marker_bdfb9c34132cd5f3452a74b3cb52ad1f.bindPopup(popup_7fb2edff3c7b86444954c7d989baf7cf)
        ;

        
    
    
            var marker_99d5ad9c802dc6a71a242fceaef16c9a = L.marker(
                [-18.9253919, -48.1997717],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_288c85cb4552e43041253b77b31293f6 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_99d5ad9c802dc6a71a242fceaef16c9a.setIcon(icon_288c85cb4552e43041253b77b31293f6);
        
    
        var popup_cf0095f88293d9f2db65d53c94d66ef4 = L.popup({"maxWidth": "100%"});

        
            
                var html_2b2258202ee5f9b83ff3a1da5868029f = $(`<div id="html_2b2258202ee5f9b83ff3a1da5868029f" style="width: 100.0%; height: 100.0%;">EE LOURDES DE CARVALHO---</div>`)[0];
                popup_cf0095f88293d9f2db65d53c94d66ef4.setContent(html_2b2258202ee5f9b83ff3a1da5868029f);
            
        

        marker_99d5ad9c802dc6a71a242fceaef16c9a.bindPopup(popup_cf0095f88293d9f2db65d53c94d66ef4)
        ;

        
    
    
            var marker_b3311fca13fb3fc2a93eac6ec6edc666 = L.marker(
                [-18.9018702, -48.2731848],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_e22bf80c8280b85bf88162a1e35081c1 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_b3311fca13fb3fc2a93eac6ec6edc666.setIcon(icon_e22bf80c8280b85bf88162a1e35081c1);
        
    
        var popup_1a617d530bc3f9fd7ae7cf992bd7a08c = L.popup({"maxWidth": "100%"});

        
            
                var html_0b030072571634718cafc838b3a05eca = $(`<div id="html_0b030072571634718cafc838b3a05eca" style="width: 100.0%; height: 100.0%;">EE PROFESSORA ALICE PAES---</div>`)[0];
                popup_1a617d530bc3f9fd7ae7cf992bd7a08c.setContent(html_0b030072571634718cafc838b3a05eca);
            
        

        marker_b3311fca13fb3fc2a93eac6ec6edc666.bindPopup(popup_1a617d530bc3f9fd7ae7cf992bd7a08c)
        ;

        
    
    
            var marker_d32bb09b55e4cdb97ab4642cead7eb3e = L.marker(
                [-18.9230375, -48.2870737],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_38f99f12706ff7ccc554d0e5830eb373 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_d32bb09b55e4cdb97ab4642cead7eb3e.setIcon(icon_38f99f12706ff7ccc554d0e5830eb373);
        
    
        var popup_e96fb24a3bbeba6bed181087931822aa = L.popup({"maxWidth": "100%"});

        
            
                var html_79d52086f154aadaddcc8e07b36f8569 = $(`<div id="html_79d52086f154aadaddcc8e07b36f8569" style="width: 100.0%; height: 100.0%;">EE BOM JESUS---</div>`)[0];
                popup_e96fb24a3bbeba6bed181087931822aa.setContent(html_79d52086f154aadaddcc8e07b36f8569);
            
        

        marker_d32bb09b55e4cdb97ab4642cead7eb3e.bindPopup(popup_e96fb24a3bbeba6bed181087931822aa)
        ;

        
    
    
            var marker_7f18dfe63b489635389c83699a30586e = L.marker(
                [-18.9437824, -48.2309653],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_cdcde1540e9be27d528572df6a60a99f = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_7f18dfe63b489635389c83699a30586e.setIcon(icon_cdcde1540e9be27d528572df6a60a99f);
        
    
        var popup_93846f0139cb2d52d6a4cccabf309366 = L.popup({"maxWidth": "100%"});

        
            
                var html_c238d10f8c061fd127cc0fe176d4f29a = $(`<div id="html_c238d10f8c061fd127cc0fe176d4f29a" style="width: 100.0%; height: 100.0%;">EE RIO DAS PEDRAS---</div>`)[0];
                popup_93846f0139cb2d52d6a4cccabf309366.setContent(html_c238d10f8c061fd127cc0fe176d4f29a);
            
        

        marker_7f18dfe63b489635389c83699a30586e.bindPopup(popup_93846f0139cb2d52d6a4cccabf309366)
        ;

        
    
    
            var marker_b7276d2aa8113556ab469dfc844da2e0 = L.marker(
                [-18.9442749, -48.2334635],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_26a8202670d84d66c4410aacf504a0f3 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_b7276d2aa8113556ab469dfc844da2e0.setIcon(icon_26a8202670d84d66c4410aacf504a0f3);
        
    
        var popup_7f015712891381f18e61b1900af4379c = L.popup({"maxWidth": "100%"});

        
            
                var html_3a779539e294bd906009718700f2379c = $(`<div id="html_3a779539e294bd906009718700f2379c" style="width: 100.0%; height: 100.0%;">EE PROFESSOR INACIO CASTILHO---</div>`)[0];
                popup_7f015712891381f18e61b1900af4379c.setContent(html_3a779539e294bd906009718700f2379c);
            
        

        marker_b7276d2aa8113556ab469dfc844da2e0.bindPopup(popup_7f015712891381f18e61b1900af4379c)
        ;

        
    
    
            var marker_6067dcc5d12ffece563ead2b89e7f769 = L.marker(
                [-18.9071357, -48.2536219],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_7a66662e9c2485b3da77b3ad0ba7486e = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_6067dcc5d12ffece563ead2b89e7f769.setIcon(icon_7a66662e9c2485b3da77b3ad0ba7486e);
        
    
        var popup_b31edbbba22578295e6e48dd6f3d42df = L.popup({"maxWidth": "100%"});

        
            
                var html_1165b315bbca30671296bdf5a527736b = $(`<div id="html_1165b315bbca30671296bdf5a527736b" style="width: 100.0%; height: 100.0%;">EE ROTARY---</div>`)[0];
                popup_b31edbbba22578295e6e48dd6f3d42df.setContent(html_1165b315bbca30671296bdf5a527736b);
            
        

        marker_6067dcc5d12ffece563ead2b89e7f769.bindPopup(popup_b31edbbba22578295e6e48dd6f3d42df)
        ;

        
    
    
            var marker_047649534e6230198a4e49b5f99d8e3d = L.marker(
                [-18.9209227, -48.27871769999999],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_c3e7f29d02b2da90b2e7d12989816b98 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_047649534e6230198a4e49b5f99d8e3d.setIcon(icon_c3e7f29d02b2da90b2e7d12989816b98);
        
    
        var popup_8e3378349cb5295ee4ab9e5d740c822b = L.popup({"maxWidth": "100%"});

        
            
                var html_c57de5417ae27cdaa06c465af3f472e5 = $(`<div id="html_c57de5417ae27cdaa06c465af3f472e5" style="width: 100.0%; height: 100.0%;">EE BUENO BRANDAO---</div>`)[0];
                popup_8e3378349cb5295ee4ab9e5d740c822b.setContent(html_c57de5417ae27cdaa06c465af3f472e5);
            
        

        marker_047649534e6230198a4e49b5f99d8e3d.bindPopup(popup_8e3378349cb5295ee4ab9e5d740c822b)
        ;

        
    
    
            var marker_c92d8ef52b615de9ca4a6b1709aec709 = L.marker(
                [-18.9108712, -48.2664556],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_e931ebd9305cc7ef4b9ce37934a23db5 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_c92d8ef52b615de9ca4a6b1709aec709.setIcon(icon_e931ebd9305cc7ef4b9ce37934a23db5);
        
    
        var popup_5b14914543c1da50b8e77876b41f517d = L.popup({"maxWidth": "100%"});

        
            
                var html_3c9b95d246b5aee62b11c2f63b1c5742 = $(`<div id="html_3c9b95d246b5aee62b11c2f63b1c5742" style="width: 100.0%; height: 100.0%;">EE SEIS DE JUNHO---</div>`)[0];
                popup_5b14914543c1da50b8e77876b41f517d.setContent(html_3c9b95d246b5aee62b11c2f63b1c5742);
            
        

        marker_c92d8ef52b615de9ca4a6b1709aec709.bindPopup(popup_5b14914543c1da50b8e77876b41f517d)
        ;

        
    
    
            var marker_bd17efb332df1f425301a930d181a4b1 = L.marker(
                [-18.9278966, -48.2264186],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_c6bf7d82bbcff7ef45d3ec8799930598 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_bd17efb332df1f425301a930d181a4b1.setIcon(icon_c6bf7d82bbcff7ef45d3ec8799930598);
        
    
        var popup_27dad58f988193e0951b3ab0d8b705f7 = L.popup({"maxWidth": "100%"});

        
            
                var html_5bb2fb9a931a885f4f47d982d6ecba68 = $(`<div id="html_5bb2fb9a931a885f4f47d982d6ecba68" style="width: 100.0%; height: 100.0%;">EE FREI EGIDIO PARISI---</div>`)[0];
                popup_27dad58f988193e0951b3ab0d8b705f7.setContent(html_5bb2fb9a931a885f4f47d982d6ecba68);
            
        

        marker_bd17efb332df1f425301a930d181a4b1.bindPopup(popup_27dad58f988193e0951b3ab0d8b705f7)
        ;

        
    
    
            var marker_5909ac9bfc519b98fbd0c539409977b0 = L.marker(
                [-18.9051564, -48.257355],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_5c89bd08101c1a93b87ef22ea7e6f740 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_5909ac9bfc519b98fbd0c539409977b0.setIcon(icon_5c89bd08101c1a93b87ef22ea7e6f740);
        
    
        var popup_0243b703626ab7edb07da9b6406c97ac = L.popup({"maxWidth": "100%"});

        
            
                var html_bdcbd8b2a7b9455bd4d4095977b7f1e0 = $(`<div id="html_bdcbd8b2a7b9455bd4d4095977b7f1e0" style="width: 100.0%; height: 100.0%;">EE SERGIO DE FREITAS PACHECO---</div>`)[0];
                popup_0243b703626ab7edb07da9b6406c97ac.setContent(html_bdcbd8b2a7b9455bd4d4095977b7f1e0);
            
        

        marker_5909ac9bfc519b98fbd0c539409977b0.bindPopup(popup_0243b703626ab7edb07da9b6406c97ac)
        ;

        
    
    
            var marker_331c9a9373456a7f9114108102393151 = L.marker(
                [-18.9055288, -48.31968939999999],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_c50983c05d30927ef8bc1858a029c342 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_331c9a9373456a7f9114108102393151.setIcon(icon_c50983c05d30927ef8bc1858a029c342);
        
    
        var popup_1dd1e068ca81f70a4cb171eac4cc0f8a = L.popup({"maxWidth": "100%"});

        
            
                var html_cf3b2e472f87613e0ca5546955e5714a = $(`<div id="html_cf3b2e472f87613e0ca5546955e5714a" style="width: 100.0%; height: 100.0%;">EE JERONIMO ARANTES---</div>`)[0];
                popup_1dd1e068ca81f70a4cb171eac4cc0f8a.setContent(html_cf3b2e472f87613e0ca5546955e5714a);
            
        

        marker_331c9a9373456a7f9114108102393151.bindPopup(popup_1dd1e068ca81f70a4cb171eac4cc0f8a)
        ;

        
    
    
            var marker_bff2eb467e25fabc7bc102b50b6def27 = L.marker(
                [-18.9153267, -48.24666759999999],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_d1045ff03830de57999e9d01ecef40bb = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_bff2eb467e25fabc7bc102b50b6def27.setIcon(icon_d1045ff03830de57999e9d01ecef40bb);
        
    
        var popup_5491e7a953bf51a1abb770be96035084 = L.popup({"maxWidth": "100%"});

        
            
                var html_ddcb2e01ee9e17771d99cfd7b37a63cf = $(`<div id="html_ddcb2e01ee9e17771d99cfd7b37a63cf" style="width: 100.0%; height: 100.0%;">EE SEGISMUNDO PEREIRA---</div>`)[0];
                popup_5491e7a953bf51a1abb770be96035084.setContent(html_ddcb2e01ee9e17771d99cfd7b37a63cf);
            
        

        marker_bff2eb467e25fabc7bc102b50b6def27.bindPopup(popup_5491e7a953bf51a1abb770be96035084)
        ;

        
    
    
            var marker_df120fd7389e673b20ce2ea11c4570c3 = L.marker(
                [-18.8970444, -48.2406552],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_bc5d649b066b83ddf1f304906e96c312 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_df120fd7389e673b20ce2ea11c4570c3.setIcon(icon_bc5d649b066b83ddf1f304906e96c312);
        
    
        var popup_e49d405f6129177a7790f181d6b818f4 = L.popup({"maxWidth": "100%"});

        
            
                var html_d64dff98a89a6c50e4677611117190c5 = $(`<div id="html_d64dff98a89a6c50e4677611117190c5" style="width: 100.0%; height: 100.0%;">EE JOAO REZENDE---</div>`)[0];
                popup_e49d405f6129177a7790f181d6b818f4.setContent(html_d64dff98a89a6c50e4677611117190c5);
            
        

        marker_df120fd7389e673b20ce2ea11c4570c3.bindPopup(popup_e49d405f6129177a7790f181d6b818f4)
        ;

        
    
    
            var marker_b3d7b3cf8a15756c91fbd28f81727daa = L.marker(
                [-18.8998356, -48.2899725],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_31995d8f4ef2c39b9406b9dd319e1872 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_b3d7b3cf8a15756c91fbd28f81727daa.setIcon(icon_31995d8f4ef2c39b9406b9dd319e1872);
        
    
        var popup_3d4759037a0143179908527188b3e145 = L.popup({"maxWidth": "100%"});

        
            
                var html_1c3fa75002fc5b29dcfeb05d9bcdf8de = $(`<div id="html_1c3fa75002fc5b29dcfeb05d9bcdf8de" style="width: 100.0%; height: 100.0%;">EE SETE DE SETEMBRO---</div>`)[0];
                popup_3d4759037a0143179908527188b3e145.setContent(html_1c3fa75002fc5b29dcfeb05d9bcdf8de);
            
        

        marker_b3d7b3cf8a15756c91fbd28f81727daa.bindPopup(popup_3d4759037a0143179908527188b3e145)
        ;

        
    
    
            var marker_6b4f01796a16a35d09c056a7b604145d = L.marker(
                [-18.8738973, -48.2673113],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_7e830268af2ae6e53bc7fe801d7763f5 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_6b4f01796a16a35d09c056a7b604145d.setIcon(icon_7e830268af2ae6e53bc7fe801d7763f5);
        
    
        var popup_d4520d7d57c57a3ea49642597854fb0c = L.popup({"maxWidth": "100%"});

        
            
                var html_54dddecbecb0a81ea4971b72a036a589 = $(`<div id="html_54dddecbecb0a81ea4971b72a036a589" style="width: 100.0%; height: 100.0%;">EE DA CIDADE INDUSTRIAL---</div>`)[0];
                popup_d4520d7d57c57a3ea49642597854fb0c.setContent(html_54dddecbecb0a81ea4971b72a036a589);
            
        

        marker_6b4f01796a16a35d09c056a7b604145d.bindPopup(popup_d4520d7d57c57a3ea49642597854fb0c)
        ;

        
    
    
            var marker_a8ef15bdf85c627451f615c069f413cb = L.marker(
                [-18.9043199, -48.26853699999999],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_fb0cfc9940a319da4e878db02fb653d7 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_a8ef15bdf85c627451f615c069f413cb.setIcon(icon_fb0cfc9940a319da4e878db02fb653d7);
        
    
        var popup_bd0ccb524de749f618cfb5145e05d2a6 = L.popup({"maxWidth": "100%"});

        
            
                var html_fa90d1aaaf83d497c96d5009fe92acf0 = $(`<div id="html_fa90d1aaaf83d497c96d5009fe92acf0" style="width: 100.0%; height: 100.0%;">EE 13 DE MAIO---</div>`)[0];
                popup_bd0ccb524de749f618cfb5145e05d2a6.setContent(html_fa90d1aaaf83d497c96d5009fe92acf0);
            
        

        marker_a8ef15bdf85c627451f615c069f413cb.bindPopup(popup_bd0ccb524de749f618cfb5145e05d2a6)
        ;

        
    
    
            var marker_ca2952f62c1b61bb7e0b2aa2cec93c4a = L.marker(
                [-18.9511902, -48.3120008],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_bfbfebf396595233dc3c2dcbf94a2aae = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_ca2952f62c1b61bb7e0b2aa2cec93c4a.setIcon(icon_bfbfebf396595233dc3c2dcbf94a2aae);
        
    
        var popup_b172a605cd7735043d3eb50dbceab7f1 = L.popup({"maxWidth": "100%"});

        
            
                var html_849cf9268b84fd64ccdb1d7c7af7dcd4 = $(`<div id="html_849cf9268b84fd64ccdb1d7c7af7dcd4" style="width: 100.0%; height: 100.0%;">EE DO BAIRRO JARDIM DAS PALMEIRAS---</div>`)[0];
                popup_b172a605cd7735043d3eb50dbceab7f1.setContent(html_849cf9268b84fd64ccdb1d7c7af7dcd4);
            
        

        marker_ca2952f62c1b61bb7e0b2aa2cec93c4a.bindPopup(popup_b172a605cd7735043d3eb50dbceab7f1)
        ;

        
    
    
            var marker_ba5cde877acf20ebc1395170cbefeaf2 = L.marker(
                [-18.9099188, -48.2870542],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_a1cd47a343e7186f63b88dc91efcaae3 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_ba5cde877acf20ebc1395170cbefeaf2.setIcon(icon_a1cd47a343e7186f63b88dc91efcaae3);
        
    
        var popup_b82f7e35c393341957dfd7a49b469a7d = L.popup({"maxWidth": "100%"});

        
            
                var html_4948d6ffb7d1745cc0bc17b04f0d9fa5 = $(`<div id="html_4948d6ffb7d1745cc0bc17b04f0d9fa5" style="width: 100.0%; height: 100.0%;">EE TUBAL VILELA DA SILVA---</div>`)[0];
                popup_b82f7e35c393341957dfd7a49b469a7d.setContent(html_4948d6ffb7d1745cc0bc17b04f0d9fa5);
            
        

        marker_ba5cde877acf20ebc1395170cbefeaf2.bindPopup(popup_b82f7e35c393341957dfd7a49b469a7d)
        ;

        
    
    
            var marker_4bb122af4ee70d65b4fad9d8c0587a71 = L.marker(
                [-18.9132669, -48.2879102],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_90a1285636d327a2f27c74ac28ac7eff = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_4bb122af4ee70d65b4fad9d8c0587a71.setIcon(icon_90a1285636d327a2f27c74ac28ac7eff);
        
    
        var popup_e77737761ae98989702324237ec7144f = L.popup({"maxWidth": "100%"});

        
            
                var html_94a104f01bd4b08e697a4e92ea24459d = $(`<div id="html_94a104f01bd4b08e697a4e92ea24459d" style="width: 100.0%; height: 100.0%;">EE CLARIMUNDO CARNEIRO---</div>`)[0];
                popup_e77737761ae98989702324237ec7144f.setContent(html_94a104f01bd4b08e697a4e92ea24459d);
            
        

        marker_4bb122af4ee70d65b4fad9d8c0587a71.bindPopup(popup_e77737761ae98989702324237ec7144f)
        ;

        
    
    
            var marker_80ded8b92d28ba189fb7f1a6dc8edc89 = L.marker(
                [-18.9214422, -48.2831266],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_68be1ebeb7f74c71e3addf7bddd48ba2 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_80ded8b92d28ba189fb7f1a6dc8edc89.setIcon(icon_68be1ebeb7f74c71e3addf7bddd48ba2);
        
    
        var popup_2c12be1202d8d80dd3264e69b737c0e3 = L.popup({"maxWidth": "100%"});

        
            
                var html_e086c72f6709b6026c7b767afdb0f325 = $(`<div id="html_e086c72f6709b6026c7b767afdb0f325" style="width: 100.0%; height: 100.0%;">EE DE UBERLANDIA---</div>`)[0];
                popup_2c12be1202d8d80dd3264e69b737c0e3.setContent(html_e086c72f6709b6026c7b767afdb0f325);
            
        

        marker_80ded8b92d28ba189fb7f1a6dc8edc89.bindPopup(popup_2c12be1202d8d80dd3264e69b737c0e3)
        ;

        
    
    
            var marker_6dc3193735b4a5b20eea7a77b940782f = L.marker(
                [-18.9300584, -48.2430064],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_65004a6da1f0755418bc3eb0724e9500 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_6dc3193735b4a5b20eea7a77b940782f.setIcon(icon_65004a6da1f0755418bc3eb0724e9500);
        
    
        var popup_ef33cc1197669862b6693c74e3d4e967 = L.popup({"maxWidth": "100%"});

        
            
                var html_09341965239f721dfa0accb283fbeb4b = $(`<div id="html_09341965239f721dfa0accb283fbeb4b" style="width: 100.0%; height: 100.0%;">EE HERCILIA MARTINS REZENDE---</div>`)[0];
                popup_ef33cc1197669862b6693c74e3d4e967.setContent(html_09341965239f721dfa0accb283fbeb4b);
            
        

        marker_6dc3193735b4a5b20eea7a77b940782f.bindPopup(popup_ef33cc1197669862b6693c74e3d4e967)
        ;

        
    
    
            var marker_f292d10a183a712a8359f52ed427c18c = L.marker(
                [-18.8871388, -48.2723553],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_9657bcdf5e8ea981effb13ba7ad4cb4f = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_f292d10a183a712a8359f52ed427c18c.setIcon(icon_9657bcdf5e8ea981effb13ba7ad4cb4f);
        
    
        var popup_034183f9210c262b9ace02534a4881d8 = L.popup({"maxWidth": "100%"});

        
            
                var html_f15931bf5b75cd6e6496c4089c1f22d8 = $(`<div id="html_f15931bf5b75cd6e6496c4089c1f22d8" style="width: 100.0%; height: 100.0%;">EE PRESIDENTE TANCREDO NEVES---</div>`)[0];
                popup_034183f9210c262b9ace02534a4881d8.setContent(html_f15931bf5b75cd6e6496c4089c1f22d8);
            
        

        marker_f292d10a183a712a8359f52ed427c18c.bindPopup(popup_034183f9210c262b9ace02534a4881d8)
        ;

        
    
    
            var marker_009d7d9a412171ff4e18e9abc05fc3c3 = L.marker(
                [-18.912758, -48.2714344],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_bded5a5e0336b67ac2ea15ba2f66b303 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_009d7d9a412171ff4e18e9abc05fc3c3.setIcon(icon_bded5a5e0336b67ac2ea15ba2f66b303);
        
    
        var popup_1ea40da6149f471d42c0d78d2de997bb = L.popup({"maxWidth": "100%"});

        
            
                var html_8c11b15615f1156c942bc661525f1f5a = $(`<div id="html_8c11b15615f1156c942bc661525f1f5a" style="width: 100.0%; height: 100.0%;">EE CORONEL JOSE TEOFILO CARNEIRO---</div>`)[0];
                popup_1ea40da6149f471d42c0d78d2de997bb.setContent(html_8c11b15615f1156c942bc661525f1f5a);
            
        

        marker_009d7d9a412171ff4e18e9abc05fc3c3.bindPopup(popup_1ea40da6149f471d42c0d78d2de997bb)
        ;

        
    
    
            var marker_6dcf3d2b5c506dee53ac209f68b53077 = L.marker(
                [-18.9324723, -48.316842],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_2b11adcf8b7d87eb214a9e2455c776ee = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_6dcf3d2b5c506dee53ac209f68b53077.setIcon(icon_2b11adcf8b7d87eb214a9e2455c776ee);
        
    
        var popup_8d6c62083ad94f709bbd72bb350470d0 = L.popup({"maxWidth": "100%"});

        
            
                var html_8e362dd6ae7fa73e0c43d4f1c9778b70 = $(`<div id="html_8e362dd6ae7fa73e0c43d4f1c9778b70" style="width: 100.0%; height: 100.0%;">EE TEOTONIO VILELA---</div>`)[0];
                popup_8d6c62083ad94f709bbd72bb350470d0.setContent(html_8e362dd6ae7fa73e0c43d4f1c9778b70);
            
        

        marker_6dcf3d2b5c506dee53ac209f68b53077.bindPopup(popup_8d6c62083ad94f709bbd72bb350470d0)
        ;

        
    
    
            var marker_ab3fd7b6e225e3430ce99a7933ba7e0f = L.marker(
                [-18.8984535, -48.336063],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_3a940e13fd679b0dcad2d6b6e9830b35 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_ab3fd7b6e225e3430ce99a7933ba7e0f.setIcon(icon_3a940e13fd679b0dcad2d6b6e9830b35);
        
    
        var popup_045b4737b93ec24207df8f3e0f2bfcd1 = L.popup({"maxWidth": "100%"});

        
            
                var html_3026ef1f42c96601ed5c95efebb23ab1 = $(`<div id="html_3026ef1f42c96601ed5c95efebb23ab1" style="width: 100.0%; height: 100.0%;">EE NEUZA REZENDE---</div>`)[0];
                popup_045b4737b93ec24207df8f3e0f2bfcd1.setContent(html_3026ef1f42c96601ed5c95efebb23ab1);
            
        

        marker_ab3fd7b6e225e3430ce99a7933ba7e0f.bindPopup(popup_045b4737b93ec24207df8f3e0f2bfcd1)
        ;

        
    
    
            var marker_acf022ee014899b4e2885f3c4256a5bb = L.marker(
                [-18.8799602, -48.2312986],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_a26476830fdd066f4c429c225d6c2ced = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_acf022ee014899b4e2885f3c4256a5bb.setIcon(icon_a26476830fdd066f4c429c225d6c2ced);
        
    
        var popup_22eb7f80eb944c44253f5752dfc0d87a = L.popup({"maxWidth": "100%"});

        
            
                var html_53e49df143494d156caa8d4ebf71916e = $(`<div id="html_53e49df143494d156caa8d4ebf71916e" style="width: 100.0%; height: 100.0%;">EE PRESIDENTE JUSCELINO KUBITSCHEK---</div>`)[0];
                popup_22eb7f80eb944c44253f5752dfc0d87a.setContent(html_53e49df143494d156caa8d4ebf71916e);
            
        

        marker_acf022ee014899b4e2885f3c4256a5bb.bindPopup(popup_22eb7f80eb944c44253f5752dfc0d87a)
        ;

        
    
    
            var marker_ac62bc9da4975f439b72d1a5e8de1eba = L.marker(
                [-18.8994424, -48.2980489],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_63f6c21fde0abde6513148f877391b1f = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_ac62bc9da4975f439b72d1a5e8de1eba.setIcon(icon_63f6c21fde0abde6513148f877391b1f);
        
    
        var popup_d33482175566c1d096706348ca19cebe = L.popup({"maxWidth": "100%"});

        
            
                var html_ebdaad14a84d97958aa77c983e82e71e = $(`<div id="html_ebdaad14a84d97958aa77c983e82e71e" style="width: 100.0%; height: 100.0%;">EE ANTONIO THOMAZ FERREIRA DE REZENDE---</div>`)[0];
                popup_d33482175566c1d096706348ca19cebe.setContent(html_ebdaad14a84d97958aa77c983e82e71e);
            
        

        marker_ac62bc9da4975f439b72d1a5e8de1eba.bindPopup(popup_d33482175566c1d096706348ca19cebe)
        ;

        
    
    
            var marker_64f607b71bb32b2761bd88ac1976d0c4 = L.marker(
                [-18.8847976, -48.2998426],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_0f5b6bfe39f4d5f0c90056aa432498c4 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_64f607b71bb32b2761bd88ac1976d0c4.setIcon(icon_0f5b6bfe39f4d5f0c90056aa432498c4);
        
    
        var popup_9516590a329ec599de2f54476c276304 = L.popup({"maxWidth": "100%"});

        
            
                var html_40d0be6f6f4d4e5719d5d6c7198e5ee2 = $(`<div id="html_40d0be6f6f4d4e5719d5d6c7198e5ee2" style="width: 100.0%; height: 100.0%;">EE DO BAIRRO MARAVILHA---</div>`)[0];
                popup_9516590a329ec599de2f54476c276304.setContent(html_40d0be6f6f4d4e5719d5d6c7198e5ee2);
            
        

        marker_64f607b71bb32b2761bd88ac1976d0c4.bindPopup(popup_9516590a329ec599de2f54476c276304)
        ;

        
    
    
            var marker_a66cda8b308a75f26a3cd50b4bbbfd3a = L.marker(
                [-18.956314, -48.2281415],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_ff30d32c7ffd6b26db498f54a4fe6e89 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_a66cda8b308a75f26a3cd50b4bbbfd3a.setIcon(icon_ff30d32c7ffd6b26db498f54a4fe6e89);
        
    
        var popup_9a478eb5d501849003b07088b4c7dd55 = L.popup({"maxWidth": "100%"});

        
            
                var html_52bc765411fac8cbae6a68025e15e4ce = $(`<div id="html_52bc765411fac8cbae6a68025e15e4ce" style="width: 100.0%; height: 100.0%;">EE DO PARQUE SAO JORGE---</div>`)[0];
                popup_9a478eb5d501849003b07088b4c7dd55.setContent(html_52bc765411fac8cbae6a68025e15e4ce);
            
        

        marker_a66cda8b308a75f26a3cd50b4bbbfd3a.bindPopup(popup_9a478eb5d501849003b07088b4c7dd55)
        ;

        
    
    
            var marker_a7dad9ee2f65d4525da10d3d4ccc4f5e = L.marker(
                [-18.9410805, -48.2343965],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_ca318547f8de5b72766b5a78f40f5223 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_a7dad9ee2f65d4525da10d3d4ccc4f5e.setIcon(icon_ca318547f8de5b72766b5a78f40f5223);
        
    
        var popup_c663ac2eff12e249691616997b5f7f3d = L.popup({"maxWidth": "100%"});

        
            
                var html_66423f72c0eb56b434eace11932f39a2 = $(`<div id="html_66423f72c0eb56b434eace11932f39a2" style="width: 100.0%; height: 100.0%;">EE DONA ALEXANDRA PEDREIRO---</div>`)[0];
                popup_c663ac2eff12e249691616997b5f7f3d.setContent(html_66423f72c0eb56b434eace11932f39a2);
            
        

        marker_a7dad9ee2f65d4525da10d3d4ccc4f5e.bindPopup(popup_c663ac2eff12e249691616997b5f7f3d)
        ;

        
    
    
            var marker_b0e2ccd650a20fe3f3570122c5f16199 = L.marker(
                [-18.9118467, -48.2779113],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_d62a617372771fad9ba0d1dbc9d5501f = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_b0e2ccd650a20fe3f3570122c5f16199.setIcon(icon_d62a617372771fad9ba0d1dbc9d5501f);
        
    
        var popup_12e265dbbfea056145cc27bce0e5785d = L.popup({"maxWidth": "100%"});

        
            
                var html_0e4380f171e39a6fbd31d75511abf5ef = $(`<div id="html_0e4380f171e39a6fbd31d75511abf5ef" style="width: 100.0%; height: 100.0%;">EE DR DUARTE PIMENTEL DE ULHOA---</div>`)[0];
                popup_12e265dbbfea056145cc27bce0e5785d.setContent(html_0e4380f171e39a6fbd31d75511abf5ef);
            
        

        marker_b0e2ccd650a20fe3f3570122c5f16199.bindPopup(popup_12e265dbbfea056145cc27bce0e5785d)
        ;

        
    
    
            var marker_b1435bf2f270764861cb322f63e57006 = L.marker(
                [-18.9095096, -48.267992],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_3622ffa125fecf901eb6a48b80004e21 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_b1435bf2f270764861cb322f63e57006.setIcon(icon_3622ffa125fecf901eb6a48b80004e21);
        
    
        var popup_708402c36470946ddc8572750ed29f92 = L.popup({"maxWidth": "100%"});

        
            
                var html_7afc4bb4e965664b40b48d8a305b8faf = $(`<div id="html_7afc4bb4e965664b40b48d8a305b8faf" style="width: 100.0%; height: 100.0%;">CESEC DE UBERLANDIA---</div>`)[0];
                popup_708402c36470946ddc8572750ed29f92.setContent(html_7afc4bb4e965664b40b48d8a305b8faf);
            
        

        marker_b1435bf2f270764861cb322f63e57006.bindPopup(popup_708402c36470946ddc8572750ed29f92)
        ;

        
    
    
            var marker_5e26595155f6a994a84f7db16fbe98e3 = L.marker(
                [-18.9186502, -48.1852848],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_33b114c5faca62b88735f441a4a4dc4b = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_5e26595155f6a994a84f7db16fbe98e3.setIcon(icon_33b114c5faca62b88735f441a4a4dc4b);
        
    
        var popup_c54a0ab0d0b6b5cb7da260dc229cd024 = L.popup({"maxWidth": "100%"});

        
            
                var html_210bc3d35ca04bce46ca812461e1ddc7 = $(`<div id="html_210bc3d35ca04bce46ca812461e1ddc7" style="width: 100.0%; height: 100.0%;">EE PROFESSOR EDERLINDO LANNES BERNARDES---</div>`)[0];
                popup_c54a0ab0d0b6b5cb7da260dc229cd024.setContent(html_210bc3d35ca04bce46ca812461e1ddc7);
            
        

        marker_5e26595155f6a994a84f7db16fbe98e3.bindPopup(popup_c54a0ab0d0b6b5cb7da260dc229cd024)
        ;

        
    
    
            var marker_813300bf4d2ab1fe7bcfc24fb47f7312 = L.marker(
                [-18.9353614, -48.2845205],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_f928e4baac40f5066811ef8c87dabcc6 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_813300bf4d2ab1fe7bcfc24fb47f7312.setIcon(icon_f928e4baac40f5066811ef8c87dabcc6);
        
    
        var popup_827ef4dc2e54cc4ce79b0710223e8d98 = L.popup({"maxWidth": "100%"});

        
            
                var html_6c8d4d6d491a04b610e9bd38124991f7 = $(`<div id="html_6c8d4d6d491a04b610e9bd38124991f7" style="width: 100.0%; height: 100.0%;">EE NOVO HORIZONTEEDUCACAO ESPECIAL---</div>`)[0];
                popup_827ef4dc2e54cc4ce79b0710223e8d98.setContent(html_6c8d4d6d491a04b610e9bd38124991f7);
            
        

        marker_813300bf4d2ab1fe7bcfc24fb47f7312.bindPopup(popup_827ef4dc2e54cc4ce79b0710223e8d98)
        ;

        
    
    
            var marker_e02a63b72963bfa9d04df0b8c53f1a63 = L.marker(
                [-18.8861058, -48.21986039999999],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_42756949fc4ea4fcc0d65617af80fa2f = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_e02a63b72963bfa9d04df0b8c53f1a63.setIcon(icon_42756949fc4ea4fcc0d65617af80fa2f);
        
    
        var popup_24382acce59586dbcff29186d54d2ef1 = L.popup({"maxWidth": "100%"});

        
            
                var html_fd3a41fef03e47881f5d2764bc432aad = $(`<div id="html_fd3a41fef03e47881f5d2764bc432aad" style="width: 100.0%; height: 100.0%;">EE JARDIM IPANEMA---</div>`)[0];
                popup_24382acce59586dbcff29186d54d2ef1.setContent(html_fd3a41fef03e47881f5d2764bc432aad);
            
        

        marker_e02a63b72963bfa9d04df0b8c53f1a63.bindPopup(popup_24382acce59586dbcff29186d54d2ef1)
        ;

        
    
    
            var marker_1c939754176e34ac018de740fc28ba3d = L.marker(
                [-18.8952722, -48.30184180000001],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_963630ebb30d35260a7c8f29bfa58d88 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_1c939754176e34ac018de740fc28ba3d.setIcon(icon_963630ebb30d35260a7c8f29bfa58d88);
        
    
        var popup_40b1b89e76e9d846e29f19de417d1af4 = L.popup({"maxWidth": "100%"});

        
            
                var html_8830a6fb80b8aa8abb172afa001b904f = $(`<div id="html_8830a6fb80b8aa8abb172afa001b904f" style="width: 100.0%; height: 100.0%;">E M AFRANIO RODRIGUES DA CUNHA---</div>`)[0];
                popup_40b1b89e76e9d846e29f19de417d1af4.setContent(html_8830a6fb80b8aa8abb172afa001b904f);
            
        

        marker_1c939754176e34ac018de740fc28ba3d.bindPopup(popup_40b1b89e76e9d846e29f19de417d1af4)
        ;

        
    
    
            var marker_8e3ea1934a46709e46709cd8bd24bdbb = L.marker(
                [-18.9759522, -48.308664],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_943504a948dce6a4b41c11a546fcb011 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_8e3ea1934a46709e46709cd8bd24bdbb.setIcon(icon_943504a948dce6a4b41c11a546fcb011);
        
    
        var popup_95991bde6727294d25d44feffae01367 = L.popup({"maxWidth": "100%"});

        
            
                var html_56c8ef0cf760f55277c9e2f24ca388ae = $(`<div id="html_56c8ef0cf760f55277c9e2f24ca388ae" style="width: 100.0%; height: 100.0%;">E M CARLOS TUCCI---</div>`)[0];
                popup_95991bde6727294d25d44feffae01367.setContent(html_56c8ef0cf760f55277c9e2f24ca388ae);
            
        

        marker_8e3ea1934a46709e46709cd8bd24bdbb.bindPopup(popup_95991bde6727294d25d44feffae01367)
        ;

        
    
    
            var marker_6acc6258dc53564ccbe6ad915321844d = L.marker(
                [-18.9253919, -48.1997717],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_f977dcb29bcb6ac19bdbd4301c5c55e9 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_6acc6258dc53564ccbe6ad915321844d.setIcon(icon_f977dcb29bcb6ac19bdbd4301c5c55e9);
        
    
        var popup_fe69eed94283bade07d0f5dd4eb2f7f7 = L.popup({"maxWidth": "100%"});

        
            
                var html_5da3b50944db780b434fdc8de538ae01 = $(`<div id="html_5da3b50944db780b434fdc8de538ae01" style="width: 100.0%; height: 100.0%;">EMEI DO CONJUNTO ALVORADA---</div>`)[0];
                popup_fe69eed94283bade07d0f5dd4eb2f7f7.setContent(html_5da3b50944db780b434fdc8de538ae01);
            
        

        marker_6acc6258dc53564ccbe6ad915321844d.bindPopup(popup_fe69eed94283bade07d0f5dd4eb2f7f7)
        ;

        
    
    
            var marker_93a0c21b8f8072eec3873c9be1ff578b = L.marker(
                [-18.9291758, -48.2523387],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_9b157ddef47d3d5a97914aac4ef239f5 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_93a0c21b8f8072eec3873c9be1ff578b.setIcon(icon_9b157ddef47d3d5a97914aac4ef239f5);
        
    
        var popup_90a6da576c6e8b8b3731260c6a3cdf54 = L.popup({"maxWidth": "100%"});

        
            
                var html_004a2db77c1b0dd8e64a600a60b7875a = $(`<div id="html_004a2db77c1b0dd8e64a600a60b7875a" style="width: 100.0%; height: 100.0%;">ESCOLA MUNICIPAL PROFESSORA GLAUCIA SANTOS MONTEIRO---</div>`)[0];
                popup_90a6da576c6e8b8b3731260c6a3cdf54.setContent(html_004a2db77c1b0dd8e64a600a60b7875a);
            
        

        marker_93a0c21b8f8072eec3873c9be1ff578b.bindPopup(popup_90a6da576c6e8b8b3731260c6a3cdf54)
        ;

        
    
    
            var marker_bff107a492ba14196a6e2debedf8b280 = L.marker(
                [-18.900182, -48.2839581],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_158e61fa91eeac29236d37d1edb6cff3 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_bff107a492ba14196a6e2debedf8b280.setIcon(icon_158e61fa91eeac29236d37d1edb6cff3);
        
    
        var popup_fc41ab323016eef1e440765d90104d4f = L.popup({"maxWidth": "100%"});

        
            
                var html_31492dcbff283d896d14cbc36b250444 = $(`<div id="html_31492dcbff283d896d14cbc36b250444" style="width: 100.0%; height: 100.0%;">E M PROFª MARIA LEONOR DE FREITAS BARBOSA---</div>`)[0];
                popup_fc41ab323016eef1e440765d90104d4f.setContent(html_31492dcbff283d896d14cbc36b250444);
            
        

        marker_bff107a492ba14196a6e2debedf8b280.bindPopup(popup_fc41ab323016eef1e440765d90104d4f)
        ;

        
    
    
            var marker_7ba4cd2ed0e8080b8fb20512744f5b3d = L.marker(
                [-18.9048095, -48.2476707],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_03fd6a7a90248f774ada7697cf16bc35 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_7ba4cd2ed0e8080b8fb20512744f5b3d.setIcon(icon_03fd6a7a90248f774ada7697cf16bc35);
        
    
        var popup_7f9944584ee3a5948b1408d32c0163cb = L.popup({"maxWidth": "100%"});

        
            
                var html_19cdda57063534f50f28d1493f34bdda = $(`<div id="html_19cdda57063534f50f28d1493f34bdda" style="width: 100.0%; height: 100.0%;">EMEI PROFª CARMELITA VIEIRA DOS SANTOS---</div>`)[0];
                popup_7f9944584ee3a5948b1408d32c0163cb.setContent(html_19cdda57063534f50f28d1493f34bdda);
            
        

        marker_7ba4cd2ed0e8080b8fb20512744f5b3d.bindPopup(popup_7f9944584ee3a5948b1408d32c0163cb)
        ;

        
    
    
            var marker_bbbee973ac110bda472f0e909fb5c121 = L.marker(
                [-18.9446307, -48.2315704],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_f3d4a1df68172aeeb701a91db2dbf571 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_bbbee973ac110bda472f0e909fb5c121.setIcon(icon_f3d4a1df68172aeeb701a91db2dbf571);
        
    
        var popup_9d0d825a07c83aaddc23eb8fc14076d6 = L.popup({"maxWidth": "100%"});

        
            
                var html_463026eb0abcb967b153d9c4f1f4a07f = $(`<div id="html_463026eb0abcb967b153d9c4f1f4a07f" style="width: 100.0%; height: 100.0%;">EMEI DOUTOR JOSE RIBEIRO---</div>`)[0];
                popup_9d0d825a07c83aaddc23eb8fc14076d6.setContent(html_463026eb0abcb967b153d9c4f1f4a07f);
            
        

        marker_bbbee973ac110bda472f0e909fb5c121.bindPopup(popup_9d0d825a07c83aaddc23eb8fc14076d6)
        ;

        
    
    
            var marker_ab9abdb85c3c78bfa5f09ef0e8965a19 = L.marker(
                [-18.8989689, -48.3378155],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_ccbd9946ead1f9db482696aa152ace85 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_ab9abdb85c3c78bfa5f09ef0e8965a19.setIcon(icon_ccbd9946ead1f9db482696aa152ace85);
        
    
        var popup_491633c7754c0f97dde86db405d4ba87 = L.popup({"maxWidth": "100%"});

        
            
                var html_d6d83800e513f25dd456d88f0fe82078 = $(`<div id="html_d6d83800e513f25dd456d88f0fe82078" style="width: 100.0%; height: 100.0%;">E M BOA VISTA---</div>`)[0];
                popup_491633c7754c0f97dde86db405d4ba87.setContent(html_d6d83800e513f25dd456d88f0fe82078);
            
        

        marker_ab9abdb85c3c78bfa5f09ef0e8965a19.bindPopup(popup_491633c7754c0f97dde86db405d4ba87)
        ;

        
    
    
            var marker_8f5b7f979e28bf2dd39f4e0d41cd65d6 = L.marker(
                [-18.9024198, -48.2770802],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_a6761b93f76e56c9a0be12b3031e17cb = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_8f5b7f979e28bf2dd39f4e0d41cd65d6.setIcon(icon_a6761b93f76e56c9a0be12b3031e17cb);
        
    
        var popup_fcdd62b5ddbf87527861bdda435beac9 = L.popup({"maxWidth": "100%"});

        
            
                var html_28b0c865baa001bd6ece3a20243fa4d5 = $(`<div id="html_28b0c865baa001bd6ece3a20243fa4d5" style="width: 100.0%; height: 100.0%;">E M DO MORENO---</div>`)[0];
                popup_fcdd62b5ddbf87527861bdda435beac9.setContent(html_28b0c865baa001bd6ece3a20243fa4d5);
            
        

        marker_8f5b7f979e28bf2dd39f4e0d41cd65d6.bindPopup(popup_fcdd62b5ddbf87527861bdda435beac9)
        ;

        
    
    
            var marker_591ee5bd58549d19d526abaa792cf15d = L.marker(
                [-18.9199679, -48.27180389999999],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_0d8d8273e2888118d5c4d965e7951843 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_591ee5bd58549d19d526abaa792cf15d.setIcon(icon_0d8d8273e2888118d5c4d965e7951843);
        
    
        var popup_9329178c68b40719a8adcb6c3703981e = L.popup({"maxWidth": "100%"});

        
            
                var html_b652a54582a7509b85fdbc4c7d82ea62 = $(`<div id="html_b652a54582a7509b85fdbc4c7d82ea62" style="width: 100.0%; height: 100.0%;">EMEI PROFª STELA MARIA DE PAIVA CARRIJO---</div>`)[0];
                popup_9329178c68b40719a8adcb6c3703981e.setContent(html_b652a54582a7509b85fdbc4c7d82ea62);
            
        

        marker_591ee5bd58549d19d526abaa792cf15d.bindPopup(popup_9329178c68b40719a8adcb6c3703981e)
        ;

        
    
    
            var marker_1a001a4275b94b33f5490b46fccf38c3 = L.marker(
                [-18.9127749, -48.2755227],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_f32b95b670c38aa0ab6c1c4b76fea37b = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_1a001a4275b94b33f5490b46fccf38c3.setIcon(icon_f32b95b670c38aa0ab6c1c4b76fea37b);
        
    
        var popup_a9ed2ad51a7c348ffc298cea61fb665c = L.popup({"maxWidth": "100%"});

        
            
                var html_0879f70f9fe3f9f653ca1be6d9a03195 = $(`<div id="html_0879f70f9fe3f9f653ca1be6d9a03195" style="width: 100.0%; height: 100.0%;">ESCOLA MUNICIPAL EMILIO RIBAS---</div>`)[0];
                popup_a9ed2ad51a7c348ffc298cea61fb665c.setContent(html_0879f70f9fe3f9f653ca1be6d9a03195);
            
        

        marker_1a001a4275b94b33f5490b46fccf38c3.bindPopup(popup_a9ed2ad51a7c348ffc298cea61fb665c)
        ;

        
    
    
            var marker_9b218a5ca8e30bce3b86211831102b39 = L.marker(
                [-18.9046776, -48.3182378],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_d5afab2ca8d61f476b7e6c0255dbacec = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_9b218a5ca8e30bce3b86211831102b39.setIcon(icon_d5afab2ca8d61f476b7e6c0255dbacec);
        
    
        var popup_63c8a072d20f7cf228e24636c95f2cb8 = L.popup({"maxWidth": "100%"});

        
            
                var html_5644e4a1930a2f4aa1a48e1a4dd44683 = $(`<div id="html_5644e4a1930a2f4aa1a48e1a4dd44683" style="width: 100.0%; height: 100.0%;">ESCOLA MUNICIPAL GUARDA ANTONIO RODRIGUES DO NASCIMENTO---</div>`)[0];
                popup_63c8a072d20f7cf228e24636c95f2cb8.setContent(html_5644e4a1930a2f4aa1a48e1a4dd44683);
            
        

        marker_9b218a5ca8e30bce3b86211831102b39.bindPopup(popup_63c8a072d20f7cf228e24636c95f2cb8)
        ;

        
    
    
            var marker_f08291527058fc336cb3584bef75670b = L.marker(
                [-18.8965405, -48.2390067],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_34d1cd8c2a4abfdd4d81cff56bf4883f = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_f08291527058fc336cb3584bef75670b.setIcon(icon_34d1cd8c2a4abfdd4d81cff56bf4883f);
        
    
        var popup_9bb7025b0d65a25375b6287067a46fff = L.popup({"maxWidth": "100%"});

        
            
                var html_61ff4cda16fa7fca3567193794f8273f = $(`<div id="html_61ff4cda16fa7fca3567193794f8273f" style="width: 100.0%; height: 100.0%;">ESCOLA MUNICIPAL PROFESSOR OSWALDO VIEIRA GONCALVES---</div>`)[0];
                popup_9bb7025b0d65a25375b6287067a46fff.setContent(html_61ff4cda16fa7fca3567193794f8273f);
            
        

        marker_f08291527058fc336cb3584bef75670b.bindPopup(popup_9bb7025b0d65a25375b6287067a46fff)
        ;

        
    
    
            var marker_fef816c77370b19edf0cae1d6691f87d = L.marker(
                [-18.9881483, -48.37419300000001],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_6c1763a1c1d60e9ae35642bb28f980b9 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_fef816c77370b19edf0cae1d6691f87d.setIcon(icon_6c1763a1c1d60e9ae35642bb28f980b9);
        
    
        var popup_6c3227b559a6f7d1111277d51e9356d9 = L.popup({"maxWidth": "100%"});

        
            
                var html_a940bb3e4f04286838115b9e2f8ac055 = $(`<div id="html_a940bb3e4f04286838115b9e2f8ac055" style="width: 100.0%; height: 100.0%;">E M FREITAS AZEVEDO---</div>`)[0];
                popup_6c3227b559a6f7d1111277d51e9356d9.setContent(html_a940bb3e4f04286838115b9e2f8ac055);
            
        

        marker_fef816c77370b19edf0cae1d6691f87d.bindPopup(popup_6c3227b559a6f7d1111277d51e9356d9)
        ;

        
    
    
            var marker_3be336f74fdf65873bba0826f9c32ecd = L.marker(
                [-18.8785115, -48.2809847],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_0caa60b49dbd436cb44745a5ee4514b8 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_3be336f74fdf65873bba0826f9c32ecd.setIcon(icon_0caa60b49dbd436cb44745a5ee4514b8);
        
    
        var popup_9d449376ea3ef015ae537648f6bea3b8 = L.popup({"maxWidth": "100%"});

        
            
                var html_e941408f1c30d062349ca9f96f2db13b = $(`<div id="html_e941408f1c30d062349ca9f96f2db13b" style="width: 100.0%; height: 100.0%;">EMEI IRMA MARIA APPARECIDA MONTEIRO---</div>`)[0];
                popup_9d449376ea3ef015ae537648f6bea3b8.setContent(html_e941408f1c30d062349ca9f96f2db13b);
            
        

        marker_3be336f74fdf65873bba0826f9c32ecd.bindPopup(popup_9d449376ea3ef015ae537648f6bea3b8)
        ;

        
    
    
            var marker_a2956ca483cd305a8de3441a435c480e = L.marker(
                [-18.9210951, -48.2482365],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_f7b0d8a87a6f0613f75153c01cb3d8a8 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_a2956ca483cd305a8de3441a435c480e.setIcon(icon_f7b0d8a87a6f0613f75153c01cb3d8a8);
        
    
        var popup_2049464204e0b00a41fca0c9e0f469f3 = L.popup({"maxWidth": "100%"});

        
            
                var html_8eb1b1455cc056caa9f8f0c49c3515b6 = $(`<div id="html_8eb1b1455cc056caa9f8f0c49c3515b6" style="width: 100.0%; height: 100.0%;">EMEI DO BAIRRO SANTA MONICA---</div>`)[0];
                popup_2049464204e0b00a41fca0c9e0f469f3.setContent(html_8eb1b1455cc056caa9f8f0c49c3515b6);
            
        

        marker_a2956ca483cd305a8de3441a435c480e.bindPopup(popup_2049464204e0b00a41fca0c9e0f469f3)
        ;

        
    
    
            var marker_dccdcaae592cbe302c4ff784625cf6f9 = L.marker(
                [-18.932752, -48.22946],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_fa485708c6ef1f5872663d011244d81e = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_dccdcaae592cbe302c4ff784625cf6f9.setIcon(icon_fa485708c6ef1f5872663d011244d81e);
        
    
        var popup_51bf8d029a71c138fcacd8e6432bd714 = L.popup({"maxWidth": "100%"});

        
            
                var html_3bdbe3fe884b525dbbd62a719eeafa45 = $(`<div id="html_3bdbe3fe884b525dbbd62a719eeafa45" style="width: 100.0%; height: 100.0%;">EMEI CECILIA MEIRELES---</div>`)[0];
                popup_51bf8d029a71c138fcacd8e6432bd714.setContent(html_3bdbe3fe884b525dbbd62a719eeafa45);
            
        

        marker_dccdcaae592cbe302c4ff784625cf6f9.bindPopup(popup_51bf8d029a71c138fcacd8e6432bd714)
        ;

        
    
    
            var marker_052de13b8e7e58e5850bb8f77932d41e = L.marker(
                [-18.8915201, -48.1447399],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_375f17fe1276714e839d3648bafe7184 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_052de13b8e7e58e5850bb8f77932d41e.setIcon(icon_375f17fe1276714e839d3648bafe7184);
        
    
        var popup_1cf5ff156e7878cdecc6d3fb684fbcbd = L.popup({"maxWidth": "100%"});

        
            
                var html_cfa970a745d145b7d1271243d7aed842 = $(`<div id="html_cfa970a745d145b7d1271243d7aed842" style="width: 100.0%; height: 100.0%;">ESCOLA MUNICIPAL OLHOS DAGUA---</div>`)[0];
                popup_1cf5ff156e7878cdecc6d3fb684fbcbd.setContent(html_cfa970a745d145b7d1271243d7aed842);
            
        

        marker_052de13b8e7e58e5850bb8f77932d41e.bindPopup(popup_1cf5ff156e7878cdecc6d3fb684fbcbd)
        ;

        
    
    
            var marker_db13aeef1da52e225a7cc53e27dc9ac4 = L.marker(
                [-18.9709689, -48.3732577],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_a1503a78bed7adf9dc1a37b6196e82ad = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_db13aeef1da52e225a7cc53e27dc9ac4.setIcon(icon_a1503a78bed7adf9dc1a37b6196e82ad);
        
    
        var popup_263c8b1161bd2091fb53a6cfc1267e76 = L.popup({"maxWidth": "100%"});

        
            
                var html_6aabba6b7cf153c83618ad798ee30aee = $(`<div id="html_6aabba6b7cf153c83618ad798ee30aee" style="width: 100.0%; height: 100.0%;">ESCOLA MUNICIPAL PROFESSORA MARIA REGINA ARANTES LEMES---</div>`)[0];
                popup_263c8b1161bd2091fb53a6cfc1267e76.setContent(html_6aabba6b7cf153c83618ad798ee30aee);
            
        

        marker_db13aeef1da52e225a7cc53e27dc9ac4.bindPopup(popup_263c8b1161bd2091fb53a6cfc1267e76)
        ;

        
    
    
            var marker_f549b2bee573e32b2f947fe2c65cd384 = L.marker(
                [-18.7272357, -48.3688128],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_70d03f2175d2530d831f9c912a7e0e76 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_f549b2bee573e32b2f947fe2c65cd384.setIcon(icon_70d03f2175d2530d831f9c912a7e0e76);
        
    
        var popup_5a18bf0b6f30f4fe6650ecb59cffabe2 = L.popup({"maxWidth": "100%"});

        
            
                var html_1e892d8b84383aea48c0863d1456ff8e = $(`<div id="html_1e892d8b84383aea48c0863d1456ff8e" style="width: 100.0%; height: 100.0%;">ESCOLA MUNICIPAL JOSE MARRA DA FONSECA---</div>`)[0];
                popup_5a18bf0b6f30f4fe6650ecb59cffabe2.setContent(html_1e892d8b84383aea48c0863d1456ff8e);
            
        

        marker_f549b2bee573e32b2f947fe2c65cd384.bindPopup(popup_5a18bf0b6f30f4fe6650ecb59cffabe2)
        ;

        
    
    
            var marker_c569a36596c082b2d6dc4cad793bf9ea = L.marker(
                [-18.7486205, -48.4195943],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_87c6b776eed33c23609d8ff5d19afb41 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_c569a36596c082b2d6dc4cad793bf9ea.setIcon(icon_87c6b776eed33c23609d8ff5d19afb41);
        
    
        var popup_8f7c32faa77cbcfe67958d7bdac65588 = L.popup({"maxWidth": "100%"});

        
            
                var html_d8256e074526d1a692890ee1d2fa8143 = $(`<div id="html_d8256e074526d1a692890ee1d2fa8143" style="width: 100.0%; height: 100.0%;">ESCOLA MUNICIPAL ANTONINO MARTINS DA SILVA---</div>`)[0];
                popup_8f7c32faa77cbcfe67958d7bdac65588.setContent(html_d8256e074526d1a692890ee1d2fa8143);
            
        

        marker_c569a36596c082b2d6dc4cad793bf9ea.bindPopup(popup_8f7c32faa77cbcfe67958d7bdac65588)
        ;

        
    
    
            var marker_7330e594513b218248de5cfdd62856a7 = L.marker(
                [-19.252115, -48.42732969999999],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_de3ad9d0af63659b411919ba8ff281e7 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_7330e594513b218248de5cfdd62856a7.setIcon(icon_de3ad9d0af63659b411919ba8ff281e7);
        
    
        var popup_3b25fb8e11aab5707c137a1fbec49cd0 = L.popup({"maxWidth": "100%"});

        
            
                var html_933d630435830ab52c3ad35fea040bc5 = $(`<div id="html_933d630435830ab52c3ad35fea040bc5" style="width: 100.0%; height: 100.0%;">E M DOMINGAS CAMIN---</div>`)[0];
                popup_3b25fb8e11aab5707c137a1fbec49cd0.setContent(html_933d630435830ab52c3ad35fea040bc5);
            
        

        marker_7330e594513b218248de5cfdd62856a7.bindPopup(popup_3b25fb8e11aab5707c137a1fbec49cd0)
        ;

        
    
    
            var marker_6fb111885b48cea4a59a31fb716cfbd5 = L.marker(
                [-19.1415143, -47.935136],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_07f0e9d335402bb7f3da682121786842 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_6fb111885b48cea4a59a31fb716cfbd5.setIcon(icon_07f0e9d335402bb7f3da682121786842);
        
    
        var popup_b9dd4648e9f7b964686d03d4413442e1 = L.popup({"maxWidth": "100%"});

        
            
                var html_354262a637c5e3b6061b1eccd1babaa9 = $(`<div id="html_354262a637c5e3b6061b1eccd1babaa9" style="width: 100.0%; height: 100.0%;">ESCOLA MUNICIPAL SEBASTIAO RANGEL---</div>`)[0];
                popup_b9dd4648e9f7b964686d03d4413442e1.setContent(html_354262a637c5e3b6061b1eccd1babaa9);
            
        

        marker_6fb111885b48cea4a59a31fb716cfbd5.bindPopup(popup_b9dd4648e9f7b964686d03d4413442e1)
        ;

        
    
    
            var marker_27715d4a452eeb6a1ab49e7cbd1e22e4 = L.marker(
                [-18.9215759, -48.329904],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_63e38c5e1d5b75570eabe9041dc6f01a = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_27715d4a452eeb6a1ab49e7cbd1e22e4.setIcon(icon_63e38c5e1d5b75570eabe9041dc6f01a);
        
    
        var popup_be2ce897ee212e17c15f5be46c5d710c = L.popup({"maxWidth": "100%"});

        
            
                var html_70ee8f3cbf0b171a1f797dd519e8e75c = $(`<div id="html_70ee8f3cbf0b171a1f797dd519e8e75c" style="width: 100.0%; height: 100.0%;">EE JOSE GOMES JUNQUEIRA---</div>`)[0];
                popup_be2ce897ee212e17c15f5be46c5d710c.setContent(html_70ee8f3cbf0b171a1f797dd519e8e75c);
            
        

        marker_27715d4a452eeb6a1ab49e7cbd1e22e4.bindPopup(popup_be2ce897ee212e17c15f5be46c5d710c)
        ;

        
    
    
            var marker_e1d0e788729b02bdbc49b97fb639996b = L.marker(
                [-18.926841, -48.190781],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_bda9b02d62be8957e682cc15ad176c2d = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_e1d0e788729b02bdbc49b97fb639996b.setIcon(icon_bda9b02d62be8957e682cc15ad176c2d);
        
    
        var popup_49267bac969d200dc09511716e31998c = L.popup({"maxWidth": "100%"});

        
            
                var html_b7c8fc4357a096fd09c3796cfcea20d0 = $(`<div id="html_b7c8fc4357a096fd09c3796cfcea20d0" style="width: 100.0%; height: 100.0%;">E M DOM BOSCO---</div>`)[0];
                popup_49267bac969d200dc09511716e31998c.setContent(html_b7c8fc4357a096fd09c3796cfcea20d0);
            
        

        marker_e1d0e788729b02bdbc49b97fb639996b.bindPopup(popup_49267bac969d200dc09511716e31998c)
        ;

        
    
    
            var marker_daddb5b5349874263e91d73bdf178a52 = L.marker(
                [-18.9501421, -48.3470218],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_8ca799c4e6196ac2a63e2d3628fe2ed6 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_daddb5b5349874263e91d73bdf178a52.setIcon(icon_8ca799c4e6196ac2a63e2d3628fe2ed6);
        
    
        var popup_daea38ab656e7cbe624ab20e845ec05b = L.popup({"maxWidth": "100%"});

        
            
                var html_1e0d71e473f93e58efaf22ef4dc095cd = $(`<div id="html_1e0d71e473f93e58efaf22ef4dc095cd" style="width: 100.0%; height: 100.0%;">E M LEANDRO JOSE DE OLIVEIRA---</div>`)[0];
                popup_daea38ab656e7cbe624ab20e845ec05b.setContent(html_1e0d71e473f93e58efaf22ef4dc095cd);
            
        

        marker_daddb5b5349874263e91d73bdf178a52.bindPopup(popup_daea38ab656e7cbe624ab20e845ec05b)
        ;

        
    
    
            var marker_6072d15beb06aa61de718c9a870826cd = L.marker(
                [-18.7967317, -48.3084472],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_67726aa28c17100ceed69b61750fdc9e = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_6072d15beb06aa61de718c9a870826cd.setIcon(icon_67726aa28c17100ceed69b61750fdc9e);
        
    
        var popup_2369e6e05fe20d706d279de26d68d0fc = L.popup({"maxWidth": "100%"});

        
            
                var html_d33c289cc5b32277a18610633422519b = $(`<div id="html_d33c289cc5b32277a18610633422519b" style="width: 100.0%; height: 100.0%;">E M DE SOBRADINHO---</div>`)[0];
                popup_2369e6e05fe20d706d279de26d68d0fc.setContent(html_d33c289cc5b32277a18610633422519b);
            
        

        marker_6072d15beb06aa61de718c9a870826cd.bindPopup(popup_2369e6e05fe20d706d279de26d68d0fc)
        ;

        
    
    
            var marker_75578660679c7aa22e5a6d8ffef2c305 = L.marker(
                [-18.9211984, -48.3312709],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_573c0d85c404711103b074a417c9e883 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_75578660679c7aa22e5a6d8ffef2c305.setIcon(icon_573c0d85c404711103b074a417c9e883);
        
    
        var popup_4f2271c01ee590c21b1fb71ee0a1a5c1 = L.popup({"maxWidth": "100%"});

        
            
                var html_fa7af346fa6d88dd079dc48eed7ca0d1 = $(`<div id="html_fa7af346fa6d88dd079dc48eed7ca0d1" style="width: 100.0%; height: 100.0%;">EMEI DO BAIRRO LUIZOTE DE FREITAS---</div>`)[0];
                popup_4f2271c01ee590c21b1fb71ee0a1a5c1.setContent(html_fa7af346fa6d88dd079dc48eed7ca0d1);
            
        

        marker_75578660679c7aa22e5a6d8ffef2c305.bindPopup(popup_4f2271c01ee590c21b1fb71ee0a1a5c1)
        ;

        
    
    
            var marker_d875017c22239183f63dbb8fe1f68c31 = L.marker(
                [-18.8723732, -48.2683226],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_bdcdb18cdaf96c581d88fae43110ba0f = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_d875017c22239183f63dbb8fe1f68c31.setIcon(icon_bdcdb18cdaf96c581d88fae43110ba0f);
        
    
        var popup_204f11d63b98d2419040eaa9eef51d88 = L.popup({"maxWidth": "100%"});

        
            
                var html_27d792eb77abf5b1d5944ab709a87efb = $(`<div id="html_27d792eb77abf5b1d5944ab709a87efb" style="width: 100.0%; height: 100.0%;">E M PROFª BENEDITA PIMENTEL DE ULHOA ROCHA---</div>`)[0];
                popup_204f11d63b98d2419040eaa9eef51d88.setContent(html_27d792eb77abf5b1d5944ab709a87efb);
            
        

        marker_d875017c22239183f63dbb8fe1f68c31.bindPopup(popup_204f11d63b98d2419040eaa9eef51d88)
        ;

        
    
    
            var marker_b6865582ef0d7fab58394bb071a33392 = L.marker(
                [-18.9324506, -48.317665],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_dc55dd84957f5b7f397ab1914af936f5 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_b6865582ef0d7fab58394bb071a33392.setIcon(icon_dc55dd84957f5b7f397ab1914af936f5);
        
    
        var popup_bbcb437c7fa22e8d726147bf5001861f = L.popup({"maxWidth": "100%"});

        
            
                var html_2e9da2c0e8a453fea30471dd43fd16dc = $(`<div id="html_2e9da2c0e8a453fea30471dd43fd16dc" style="width: 100.0%; height: 100.0%;">E M PROFª IRACY ANDRADE JUNQUEIRA---</div>`)[0];
                popup_bbcb437c7fa22e8d726147bf5001861f.setContent(html_2e9da2c0e8a453fea30471dd43fd16dc);
            
        

        marker_b6865582ef0d7fab58394bb071a33392.bindPopup(popup_bbcb437c7fa22e8d726147bf5001861f)
        ;

        
    
    
            var marker_54054174f179a36625546341c0c18570 = L.marker(
                [-18.9524409, -48.2330496],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_415420f173051ae95696ba248419161b = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_54054174f179a36625546341c0c18570.setIcon(icon_415420f173051ae95696ba248419161b);
        
    
        var popup_59a403477c266ef91d72e16ef6a1c212 = L.popup({"maxWidth": "100%"});

        
            
                var html_ad49056d8b7b6caec4f038361207665b = $(`<div id="html_ad49056d8b7b6caec4f038361207665b" style="width: 100.0%; height: 100.0%;">E M PROF EURICO SILVA---</div>`)[0];
                popup_59a403477c266ef91d72e16ef6a1c212.setContent(html_ad49056d8b7b6caec4f038361207665b);
            
        

        marker_54054174f179a36625546341c0c18570.bindPopup(popup_59a403477c266ef91d72e16ef6a1c212)
        ;

        
    
    
            var marker_21298d68fbaf63590b58e18d4e94e69e = L.marker(
                [-18.8898757, -48.2900795],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_89b740bbfc8abf04d43dd273255bfb87 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_21298d68fbaf63590b58e18d4e94e69e.setIcon(icon_89b740bbfc8abf04d43dd273255bfb87);
        
    
        var popup_79c50b7d10c70b9658bc179961b7a92c = L.popup({"maxWidth": "100%"});

        
            
                var html_a84593f79806fdcb2fb4a8f04ef5dbde = $(`<div id="html_a84593f79806fdcb2fb4a8f04ef5dbde" style="width: 100.0%; height: 100.0%;">E M PROF SERGIO DE OLIVEIRA MARQUEZ---</div>`)[0];
                popup_79c50b7d10c70b9658bc179961b7a92c.setContent(html_a84593f79806fdcb2fb4a8f04ef5dbde);
            
        

        marker_21298d68fbaf63590b58e18d4e94e69e.bindPopup(popup_79c50b7d10c70b9658bc179961b7a92c)
        ;

        
    
    
            var marker_bd370c0d87b177f3074f4748f42bde5f = L.marker(
                [-18.9385577, -48.3103464],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_d0bf4d239ce0580f5c685e871bccd87c = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_bd370c0d87b177f3074f4748f42bde5f.setIcon(icon_d0bf4d239ce0580f5c685e871bccd87c);
        
    
        var popup_d8b994b9319a8f8ee4638f2dd26591ee = L.popup({"maxWidth": "100%"});

        
            
                var html_a395311124af5aabb04c07245e0a6aaa = $(`<div id="html_a395311124af5aabb04c07245e0a6aaa" style="width: 100.0%; height: 100.0%;">E M PROF LEONCIO DO CARMO CHAVES---</div>`)[0];
                popup_d8b994b9319a8f8ee4638f2dd26591ee.setContent(html_a395311124af5aabb04c07245e0a6aaa);
            
        

        marker_bd370c0d87b177f3074f4748f42bde5f.bindPopup(popup_d8b994b9319a8f8ee4638f2dd26591ee)
        ;

        
    
    
            var marker_f9e74f70227c47d432f9f4a13ea35a84 = L.marker(
                [-18.8933491, -48.3159669],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_e3c39be1e467176c8ac2dff8aa1a7047 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_f9e74f70227c47d432f9f4a13ea35a84.setIcon(icon_e3c39be1e467176c8ac2dff8aa1a7047);
        
    
        var popup_6e0f359b37e83faefc7b79e893bc7c7d = L.popup({"maxWidth": "100%"});

        
            
                var html_faa4d4409c56341f772e7e8ba7e80bb7 = $(`<div id="html_faa4d4409c56341f772e7e8ba7e80bb7" style="width: 100.0%; height: 100.0%;">EMEI PROFª MARIA CLARO---</div>`)[0];
                popup_6e0f359b37e83faefc7b79e893bc7c7d.setContent(html_faa4d4409c56341f772e7e8ba7e80bb7);
            
        

        marker_f9e74f70227c47d432f9f4a13ea35a84.bindPopup(popup_6e0f359b37e83faefc7b79e893bc7c7d)
        ;

        
    
    
            var marker_acbeed6437125a7007ee61b39ec339c9 = L.marker(
                [-18.947515, -48.2400137],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_dae8837a7c7b64faa5dd0a64a631cf4b = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_acbeed6437125a7007ee61b39ec339c9.setIcon(icon_dae8837a7c7b64faa5dd0a64a631cf4b);
        
    
        var popup_0bdc0e95ac3af606561bc86c2edd4216 = L.popup({"maxWidth": "100%"});

        
            
                var html_aa1cf3adec0c7bc91f234b00591f9f81 = $(`<div id="html_aa1cf3adec0c7bc91f234b00591f9f81" style="width: 100.0%; height: 100.0%;">E M PROF VALDEMAR FIRMINO DE OLIVEIRA---</div>`)[0];
                popup_0bdc0e95ac3af606561bc86c2edd4216.setContent(html_aa1cf3adec0c7bc91f234b00591f9f81);
            
        

        marker_acbeed6437125a7007ee61b39ec339c9.bindPopup(popup_0bdc0e95ac3af606561bc86c2edd4216)
        ;

        
    
    
            var marker_dc5a6999b6eb73a48d66caf72d3ded36 = L.marker(
                [-18.9421592, -48.3098598],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_f78355d5d7a70af192501666bffa8a82 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_dc5a6999b6eb73a48d66caf72d3ded36.setIcon(icon_f78355d5d7a70af192501666bffa8a82);
        
    
        var popup_e1f668bcbc793570e53a0dbf9ee7bcbd = L.popup({"maxWidth": "100%"});

        
            
                var html_29069e44a6335b02b11fd8321ff7b4d9 = $(`<div id="html_29069e44a6335b02b11fd8321ff7b4d9" style="width: 100.0%; height: 100.0%;">ESCOLA MUNICIPAL PROFESSORA MARIA JOSE MAMEDE MOREIRA---</div>`)[0];
                popup_e1f668bcbc793570e53a0dbf9ee7bcbd.setContent(html_29069e44a6335b02b11fd8321ff7b4d9);
            
        

        marker_dc5a6999b6eb73a48d66caf72d3ded36.bindPopup(popup_e1f668bcbc793570e53a0dbf9ee7bcbd)
        ;

        
    
    
            var marker_5550465766875a8e360b04692be9e51f = L.marker(
                [-18.9334279, -48.3006989],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_698dce24fb40f8811627660409e3c0d8 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_5550465766875a8e360b04692be9e51f.setIcon(icon_698dce24fb40f8811627660409e3c0d8);
        
    
        var popup_bec92b6e9fe738ca5ff6e16264bc58f6 = L.popup({"maxWidth": "100%"});

        
            
                var html_6e98de06785bd6978678cbc3382577ce = $(`<div id="html_6e98de06785bd6978678cbc3382577ce" style="width: 100.0%; height: 100.0%;">E M PROF LUIZ ROCHA E SILVA---</div>`)[0];
                popup_bec92b6e9fe738ca5ff6e16264bc58f6.setContent(html_6e98de06785bd6978678cbc3382577ce);
            
        

        marker_5550465766875a8e360b04692be9e51f.bindPopup(popup_bec92b6e9fe738ca5ff6e16264bc58f6)
        ;

        
    
    
            var marker_270dce928fbe894c18e78d92f00aaff6 = L.marker(
                [-18.9293013, -48.3347195],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_5b6f132e7071eafed442f68d4214dd08 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_270dce928fbe894c18e78d92f00aaff6.setIcon(icon_5b6f132e7071eafed442f68d4214dd08);
        
    
        var popup_d74ebff5dc5b5d91783563ecb2d3051c = L.popup({"maxWidth": "100%"});

        
            
                var html_d0ec3e9c766c81a965cbeb5bc16db5cb = $(`<div id="html_d0ec3e9c766c81a965cbeb5bc16db5cb" style="width: 100.0%; height: 100.0%;">ESCOLA MUNICIPAL PROFESSORA CECY CARDOSO PORFIRIO---</div>`)[0];
                popup_d74ebff5dc5b5d91783563ecb2d3051c.setContent(html_d0ec3e9c766c81a965cbeb5bc16db5cb);
            
        

        marker_270dce928fbe894c18e78d92f00aaff6.bindPopup(popup_d74ebff5dc5b5d91783563ecb2d3051c)
        ;

        
    
    
            var marker_c3ea711126890c1ef6d836bb7381610d = L.marker(
                [-18.9018175, -48.3384192],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_7126998cedc81500182fafc64d6a7bb1 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_c3ea711126890c1ef6d836bb7381610d.setIcon(icon_7126998cedc81500182fafc64d6a7bb1);
        
    
        var popup_55c18a66b36ebaf5fb7dc770fac78283 = L.popup({"maxWidth": "100%"});

        
            
                var html_9cb7d413fe41ad7c170b7bfe3b0ad70d = $(`<div id="html_9cb7d413fe41ad7c170b7bfe3b0ad70d" style="width: 100.0%; height: 100.0%;">ESCOLA MUNICIPAL PROFESSOR MARIO GODOY CASTANHO---</div>`)[0];
                popup_55c18a66b36ebaf5fb7dc770fac78283.setContent(html_9cb7d413fe41ad7c170b7bfe3b0ad70d);
            
        

        marker_c3ea711126890c1ef6d836bb7381610d.bindPopup(popup_55c18a66b36ebaf5fb7dc770fac78283)
        ;

        
    
    
            var marker_2a33ba75b012103d4fa598d278880c7f = L.marker(
                [-18.8898316, -48.2604273],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_c2a4a342e0a831dc392f71c1ce0863d5 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_2a33ba75b012103d4fa598d278880c7f.setIcon(icon_c2a4a342e0a831dc392f71c1ce0863d5);
        
    
        var popup_f7b2bd1936535b871957826640a6e1fa = L.popup({"maxWidth": "100%"});

        
            
                var html_7aa35eb5c890c1dc020ef3cbc9dc2230 = $(`<div id="html_7aa35eb5c890c1dc020ef3cbc9dc2230" style="width: 100.0%; height: 100.0%;">E M PROF OTAVIO BATISTA COELHO FILHO---</div>`)[0];
                popup_f7b2bd1936535b871957826640a6e1fa.setContent(html_7aa35eb5c890c1dc020ef3cbc9dc2230);
            
        

        marker_2a33ba75b012103d4fa598d278880c7f.bindPopup(popup_f7b2bd1936535b871957826640a6e1fa)
        ;

        
    
    
            var marker_ca9549924006dc9da0fb4343aef5f07d = L.marker(
                [-18.9274337, -48.2438772],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_05bd30e328085608f415524df35b3541 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_ca9549924006dc9da0fb4343aef5f07d.setIcon(icon_05bd30e328085608f415524df35b3541);
        
    
        var popup_f0a07d4ce0b22ef6089aa0795e4e2eb9 = L.popup({"maxWidth": "100%"});

        
            
                var html_a3c07a3920200a9d523e20a232a40201 = $(`<div id="html_a3c07a3920200a9d523e20a232a40201" style="width: 100.0%; height: 100.0%;">E M PROF DOMINGOS PIMENTEL DE ULHOA---</div>`)[0];
                popup_f0a07d4ce0b22ef6089aa0795e4e2eb9.setContent(html_a3c07a3920200a9d523e20a232a40201);
            
        

        marker_ca9549924006dc9da0fb4343aef5f07d.bindPopup(popup_f0a07d4ce0b22ef6089aa0795e4e2eb9)
        ;

        
    
    
            var marker_6aa63781278969cfc139ee9a2fd6cfba = L.marker(
                [-18.9083919, -48.2110978],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_69cb74f2a31344ea0e03da3488d86f58 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_6aa63781278969cfc139ee9a2fd6cfba.setIcon(icon_69cb74f2a31344ea0e03da3488d86f58);
        
    
        var popup_9a96e31596dba072caca6d377d4c46a5 = L.popup({"maxWidth": "100%"});

        
            
                var html_74599cbdb341e11835d7cea28caed974 = $(`<div id="html_74599cbdb341e11835d7cea28caed974" style="width: 100.0%; height: 100.0%;">E M DR JOEL CUPERTINO RODRIGUES---</div>`)[0];
                popup_9a96e31596dba072caca6d377d4c46a5.setContent(html_74599cbdb341e11835d7cea28caed974);
            
        

        marker_6aa63781278969cfc139ee9a2fd6cfba.bindPopup(popup_9a96e31596dba072caca6d377d4c46a5)
        ;

        
    
    
            var marker_536e7f9f924587d641a4b89d5e7918ab = L.marker(
                [-18.9175796, -48.1870519],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_78e116f3bb4bf1f811e5c31bf645f066 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_536e7f9f924587d641a4b89d5e7918ab.setIcon(icon_78e116f3bb4bf1f811e5c31bf645f066);
        
    
        var popup_0e79180d93b81f7c72170cd046454ee3 = L.popup({"maxWidth": "100%"});

        
            
                var html_f76605936d6725f4b02012275bee0c3a = $(`<div id="html_f76605936d6725f4b02012275bee0c3a" style="width: 100.0%; height: 100.0%;">E M HILDA LEAO CARNEIRO---</div>`)[0];
                popup_0e79180d93b81f7c72170cd046454ee3.setContent(html_f76605936d6725f4b02012275bee0c3a);
            
        

        marker_536e7f9f924587d641a4b89d5e7918ab.bindPopup(popup_0e79180d93b81f7c72170cd046454ee3)
        ;

        
    
    
            var marker_6dc8fdcd955380ba59edebf3cf7a6508 = L.marker(
                [-18.8745686, -48.2732463],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_410dad343d216ab4935e48d21a5cbfc5 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_6dc8fdcd955380ba59edebf3cf7a6508.setIcon(icon_410dad343d216ab4935e48d21a5cbfc5);
        
    
        var popup_20e2ca67f6018c28ed4848527731d74a = L.popup({"maxWidth": "100%"});

        
            
                var html_c28f360765a2485a2d07b529ba25671c = $(`<div id="html_c28f360765a2485a2d07b529ba25671c" style="width: 100.0%; height: 100.0%;">ESCOLA MUNICIPAL PROFESSOR LADARIO TEIXEIRA---</div>`)[0];
                popup_20e2ca67f6018c28ed4848527731d74a.setContent(html_c28f360765a2485a2d07b529ba25671c);
            
        

        marker_6dc8fdcd955380ba59edebf3cf7a6508.bindPopup(popup_20e2ca67f6018c28ed4848527731d74a)
        ;

        
    
    
            var marker_0fbb82c3e8b41c630d16feb12b1a5bee = L.marker(
                [-18.9566146, -48.24353],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_be4e6e149421c5a9b48513e2ad8744b5 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_0fbb82c3e8b41c630d16feb12b1a5bee.setIcon(icon_be4e6e149421c5a9b48513e2ad8744b5);
        
    
        var popup_1783f177b04d51aa221ad3ab273f0197 = L.popup({"maxWidth": "100%"});

        
            
                var html_2dd30c3c85bca8d131a24b50804916b6 = $(`<div id="html_2dd30c3c85bca8d131a24b50804916b6" style="width: 100.0%; height: 100.0%;">ESCOLA MUNICIPAL PROFESSORA OLGA DEL FAVERO---</div>`)[0];
                popup_1783f177b04d51aa221ad3ab273f0197.setContent(html_2dd30c3c85bca8d131a24b50804916b6);
            
        

        marker_0fbb82c3e8b41c630d16feb12b1a5bee.bindPopup(popup_1783f177b04d51aa221ad3ab273f0197)
        ;

        
    
    
            var marker_f3ab444847998a0dbaa01a60fa9607a4 = L.marker(
                [-18.8924257, -48.3313704],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_f2ff91cfc80496e6b57b7bc25764daca = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_f3ab444847998a0dbaa01a60fa9607a4.setIcon(icon_f2ff91cfc80496e6b57b7bc25764daca);
        
    
        var popup_c1cc2107598fad5365d98acbf68d6620 = L.popup({"maxWidth": "100%"});

        
            
                var html_feecd02b492c1df34a42df37cb1a2b7a = $(`<div id="html_feecd02b492c1df34a42df37cb1a2b7a" style="width: 100.0%; height: 100.0%;">ESCOLA MUNICIPAL PROFESSORA STELLA SARAIVA PEANO---</div>`)[0];
                popup_c1cc2107598fad5365d98acbf68d6620.setContent(html_feecd02b492c1df34a42df37cb1a2b7a);
            
        

        marker_f3ab444847998a0dbaa01a60fa9607a4.bindPopup(popup_c1cc2107598fad5365d98acbf68d6620)
        ;

        
    
    
            var marker_d82700df18e7acf0336a0edc38756a5e = L.marker(
                [-18.8721035, -48.2679531],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_23e358dabc3db79c7190220e236db80a = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_d82700df18e7acf0336a0edc38756a5e.setIcon(icon_23e358dabc3db79c7190220e236db80a);
        
    
        var popup_c91bcff039e845827c26865105e6c515 = L.popup({"maxWidth": "100%"});

        
            
                var html_a7d0fd5673329f44acc182f0940aa0ef = $(`<div id="html_a7d0fd5673329f44acc182f0940aa0ef" style="width: 100.0%; height: 100.0%;">EMEI MARIA BEATRIZ VILELA DE OLIVEIRA---</div>`)[0];
                popup_c91bcff039e845827c26865105e6c515.setContent(html_a7d0fd5673329f44acc182f0940aa0ef);
            
        

        marker_d82700df18e7acf0336a0edc38756a5e.bindPopup(popup_c91bcff039e845827c26865105e6c515)
        ;

        
    
    
            var marker_55189fcf0382f1e02728f9c0f4c6117a = L.marker(
                [-18.9194382, -48.302343],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_581cce7e7c9918154a37881402fb3149 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_55189fcf0382f1e02728f9c0f4c6117a.setIcon(icon_581cce7e7c9918154a37881402fb3149);
        
    
        var popup_5a914505dc9536515154e02ccd501c1a = L.popup({"maxWidth": "100%"});

        
            
                var html_ee9e78c2295625d9d8ef761483ded2dc = $(`<div id="html_ee9e78c2295625d9d8ef761483ded2dc" style="width: 100.0%; height: 100.0%;">E M SEBASTIANA SILVEIRA PINTO---</div>`)[0];
                popup_5a914505dc9536515154e02ccd501c1a.setContent(html_ee9e78c2295625d9d8ef761483ded2dc);
            
        

        marker_55189fcf0382f1e02728f9c0f4c6117a.bindPopup(popup_5a914505dc9536515154e02ccd501c1a)
        ;

        
    
    
            var marker_0aa74126ed537a930b6ccffd352df21d = L.marker(
                [-18.9433313, -48.3135968],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_11720ce998259003e3161eadf914949e = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_0aa74126ed537a930b6ccffd352df21d.setIcon(icon_11720ce998259003e3161eadf914949e);
        
    
        var popup_78ab01c73d90cc9e1d731bc45bc99de1 = L.popup({"maxWidth": "100%"});

        
            
                var html_3f116c584faa3cde63a476d557fd59fb = $(`<div id="html_3f116c584faa3cde63a476d557fd59fb" style="width: 100.0%; height: 100.0%;">EMEI PROFª EDNA APARECIDA DE OLIVEIRA---</div>`)[0];
                popup_78ab01c73d90cc9e1d731bc45bc99de1.setContent(html_3f116c584faa3cde63a476d557fd59fb);
            
        

        marker_0aa74126ed537a930b6ccffd352df21d.bindPopup(popup_78ab01c73d90cc9e1d731bc45bc99de1)
        ;

        
    
    
            var marker_0723969e90c129f5da7efa55d6cd9e90 = L.marker(
                [-18.9134472, -48.25784119999999],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_28a9bbd2990e4ca91c04ab7bebcdd6b6 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_0723969e90c129f5da7efa55d6cd9e90.setIcon(icon_28a9bbd2990e4ca91c04ab7bebcdd6b6);
        
    
        var popup_390e56c543abc49840da62b3e4d90185 = L.popup({"maxWidth": "100%"});

        
            
                var html_eaa4c80fb7defd63673ad9d8af1f08c9 = $(`<div id="html_eaa4c80fb7defd63673ad9d8af1f08c9" style="width: 100.0%; height: 100.0%;">EMEI MARIA PACHECO REZENDE---</div>`)[0];
                popup_390e56c543abc49840da62b3e4d90185.setContent(html_eaa4c80fb7defd63673ad9d8af1f08c9);
            
        

        marker_0723969e90c129f5da7efa55d6cd9e90.bindPopup(popup_390e56c543abc49840da62b3e4d90185)
        ;

        
    
    
            var marker_939db7144169a53110022d96e4966c03 = L.marker(
                [-18.886333, -48.2730876],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_e568c9f59863b2dde07f5d1e528eee0e = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_939db7144169a53110022d96e4966c03.setIcon(icon_e568c9f59863b2dde07f5d1e528eee0e);
        
    
        var popup_5464b3d4f26b88b6c63f86e2c3caa346 = L.popup({"maxWidth": "100%"});

        
            
                var html_0f0fcb07875c143212bcee9361d6e8e1 = $(`<div id="html_0f0fcb07875c143212bcee9361d6e8e1" style="width: 100.0%; height: 100.0%;">EMEI PROF THALES DE ASSIS MARTINS---</div>`)[0];
                popup_5464b3d4f26b88b6c63f86e2c3caa346.setContent(html_0f0fcb07875c143212bcee9361d6e8e1);
            
        

        marker_939db7144169a53110022d96e4966c03.bindPopup(popup_5464b3d4f26b88b6c63f86e2c3caa346)
        ;

        
    
    
            var marker_7160611648b2f7c301cf60f8f025d667 = L.marker(
                [-18.9117019, -48.181557],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_c4d04f630de29cb06aaa79a28a25a1e8 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_7160611648b2f7c301cf60f8f025d667.setIcon(icon_c4d04f630de29cb06aaa79a28a25a1e8);
        
    
        var popup_f7cd2a89d99be67d21946896e71ba945 = L.popup({"maxWidth": "100%"});

        
            
                var html_47b14d0f28cf22de293dce3fb6dcd539 = $(`<div id="html_47b14d0f28cf22de293dce3fb6dcd539" style="width: 100.0%; height: 100.0%;">E M EUGENIO PIMENTEL ARANTES---</div>`)[0];
                popup_f7cd2a89d99be67d21946896e71ba945.setContent(html_47b14d0f28cf22de293dce3fb6dcd539);
            
        

        marker_7160611648b2f7c301cf60f8f025d667.bindPopup(popup_f7cd2a89d99be67d21946896e71ba945)
        ;

        
    
    
            var marker_d701f6b4cc304bc5d2025a344b04917e = L.marker(
                [-18.8990109, -48.305077],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_f2f7fd16270f8e7b61237978d160f7a2 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_d701f6b4cc304bc5d2025a344b04917e.setIcon(icon_f2f7fd16270f8e7b61237978d160f7a2);
        
    
        var popup_33810e30cf3543b55888421313f2aee9 = L.popup({"maxWidth": "100%"});

        
            
                var html_329371a30a90be6baf8b530430339469 = $(`<div id="html_329371a30a90be6baf8b530430339469" style="width: 100.0%; height: 100.0%;">EMEI DO BAIRRO JARDIM BRASILIA---</div>`)[0];
                popup_33810e30cf3543b55888421313f2aee9.setContent(html_329371a30a90be6baf8b530430339469);
            
        

        marker_d701f6b4cc304bc5d2025a344b04917e.bindPopup(popup_33810e30cf3543b55888421313f2aee9)
        ;

        
    
    
            var marker_bc16ac83c5e5adf3ea1435e9afaecdab = L.marker(
                [-18.9533859, -48.2338141],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_dcfe4fad7c7c98b1f56a1ddb5b816f3d = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_bc16ac83c5e5adf3ea1435e9afaecdab.setIcon(icon_dcfe4fad7c7c98b1f56a1ddb5b816f3d);
        
    
        var popup_f24743c1636c8a2aa63df453b8114db2 = L.popup({"maxWidth": "100%"});

        
            
                var html_0beedbf6bf6dfc033fcf6d7146de849c = $(`<div id="html_0beedbf6bf6dfc033fcf6d7146de849c" style="width: 100.0%; height: 100.0%;">EMEI PROFª MARIA LUIZA BARBOSA DE SOUZA---</div>`)[0];
                popup_f24743c1636c8a2aa63df453b8114db2.setContent(html_0beedbf6bf6dfc033fcf6d7146de849c);
            
        

        marker_bc16ac83c5e5adf3ea1435e9afaecdab.bindPopup(popup_f24743c1636c8a2aa63df453b8114db2)
        ;

        
    
    
            var marker_7e4c34c8645a9a2b112c88738bdadfe7 = L.marker(
                [-18.9194382, -48.302343],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_eb6988df1a68d5de7ebd56ccd122af55 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_7e4c34c8645a9a2b112c88738bdadfe7.setIcon(icon_eb6988df1a68d5de7ebd56ccd122af55);
        
    
        var popup_08bcec72b40ebbb824d2201f37a6f11b = L.popup({"maxWidth": "100%"});

        
            
                var html_857b2cab6036947a009ddfe556fe21b7 = $(`<div id="html_857b2cab6036947a009ddfe556fe21b7" style="width: 100.0%; height: 100.0%;">ESCOLA MUNICIPAL PROFESSOR JACY DE ASSIS---</div>`)[0];
                popup_08bcec72b40ebbb824d2201f37a6f11b.setContent(html_857b2cab6036947a009ddfe556fe21b7);
            
        

        marker_7e4c34c8645a9a2b112c88738bdadfe7.bindPopup(popup_08bcec72b40ebbb824d2201f37a6f11b)
        ;

        
    
    
            var marker_44549c6cc93dbfbc067504c622c8fce3 = L.marker(
                [-18.959913, -48.327747],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_413f265f8e61e55a0c511acee9d1be1b = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_44549c6cc93dbfbc067504c622c8fce3.setIcon(icon_413f265f8e61e55a0c511acee9d1be1b);
        
    
        var popup_527a39dacd2d0773b15600b223233778 = L.popup({"maxWidth": "100%"});

        
            
                var html_ee88d27212fa9422d773244152988d01 = $(`<div id="html_ee88d27212fa9422d773244152988d01" style="width: 100.0%; height: 100.0%;">ESCOLA MUNICIPAL DOUTOR GLADSEN GUERRA DE REZENDE---</div>`)[0];
                popup_527a39dacd2d0773b15600b223233778.setContent(html_ee88d27212fa9422d773244152988d01);
            
        

        marker_44549c6cc93dbfbc067504c622c8fce3.bindPopup(popup_527a39dacd2d0773b15600b223233778)
        ;

        
    
    
            var marker_3b5962fc6fd95ec2f5501c2bc9db16ba = L.marker(
                [-18.8677855, -48.263877],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_4369a551639b3a16fc385929cf59b531 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_3b5962fc6fd95ec2f5501c2bc9db16ba.setIcon(icon_4369a551639b3a16fc385929cf59b531);
        
    
        var popup_86e9edf2fe8ba06f14421395b2bec9bd = L.popup({"maxWidth": "100%"});

        
            
                var html_4d0a09278772040c900e33847545caef = $(`<div id="html_4d0a09278772040c900e33847545caef" style="width: 100.0%; height: 100.0%;">EMEI PROF SAINT CLAIR NETTO---</div>`)[0];
                popup_86e9edf2fe8ba06f14421395b2bec9bd.setContent(html_4d0a09278772040c900e33847545caef);
            
        

        marker_3b5962fc6fd95ec2f5501c2bc9db16ba.bindPopup(popup_86e9edf2fe8ba06f14421395b2bec9bd)
        ;

        
    
    
            var marker_35ec36dc7c5bf26c068a2e2636fcb645 = L.marker(
                [-18.8898316, -48.2604273],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_2f06366d256fb2b8818c05fc4f81f23e = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_35ec36dc7c5bf26c068a2e2636fcb645.setIcon(icon_2f06366d256fb2b8818c05fc4f81f23e);
        
    
        var popup_16ee983b4bc9337beacf222bd358c189 = L.popup({"maxWidth": "100%"});

        
            
                var html_96396ebe133ff60aa825644d23c9b4da = $(`<div id="html_96396ebe133ff60aa825644d23c9b4da" style="width: 100.0%; height: 100.0%;">EMEI PROFESSOR HORLANDI VIOLATTI---</div>`)[0];
                popup_16ee983b4bc9337beacf222bd358c189.setContent(html_96396ebe133ff60aa825644d23c9b4da);
            
        

        marker_35ec36dc7c5bf26c068a2e2636fcb645.bindPopup(popup_16ee983b4bc9337beacf222bd358c189)
        ;

        
    
    
            var marker_b63d94857a6e5dbedc0f97ec215af4be = L.marker(
                [-18.888969, -48.26141],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_515b85a94d7cb2f3224a88f6737aec6b = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_b63d94857a6e5dbedc0f97ec215af4be.setIcon(icon_515b85a94d7cb2f3224a88f6737aec6b);
        
    
        var popup_26fbbd3f60fc10941629200e4517277a = L.popup({"maxWidth": "100%"});

        
            
                var html_c7158f7396faa8b6b40c9f922fa90ed2 = $(`<div id="html_c7158f7396faa8b6b40c9f922fa90ed2" style="width: 100.0%; height: 100.0%;">E M AMANDA CARNEIRO TEIXEIRA---</div>`)[0];
                popup_26fbbd3f60fc10941629200e4517277a.setContent(html_c7158f7396faa8b6b40c9f922fa90ed2);
            
        

        marker_b63d94857a6e5dbedc0f97ec215af4be.bindPopup(popup_26fbbd3f60fc10941629200e4517277a)
        ;

        
    
    
            var marker_a06cc63875b377dead894d559a6cd1ea = L.marker(
                [-18.9292842, -48.2272057],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_5365df53fdc2f65158cd084b43dcb4d9 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_a06cc63875b377dead894d559a6cd1ea.setIcon(icon_5365df53fdc2f65158cd084b43dcb4d9);
        
    
        var popup_31f01102074130d9d2b5c9cb8196ba31 = L.popup({"maxWidth": "100%"});

        
            
                var html_e5415cf5c6ab1e9ce83979ca9de82113 = $(`<div id="html_e5415cf5c6ab1e9ce83979ca9de82113" style="width: 100.0%; height: 100.0%;">E M PROF MILTON DE MAGALHAES PORTO---</div>`)[0];
                popup_31f01102074130d9d2b5c9cb8196ba31.setContent(html_e5415cf5c6ab1e9ce83979ca9de82113);
            
        

        marker_a06cc63875b377dead894d559a6cd1ea.bindPopup(popup_31f01102074130d9d2b5c9cb8196ba31)
        ;

        
    
    
            var marker_ad79d6ee20d766e849dd7c1b34580bdc = L.marker(
                [-18.9213609, -48.3304553],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_951488a269ca2b6aae0c3e3882870a4b = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_ad79d6ee20d766e849dd7c1b34580bdc.setIcon(icon_951488a269ca2b6aae0c3e3882870a4b);
        
    
        var popup_cf094fa14801604c77f89fdf6935e45f = L.popup({"maxWidth": "100%"});

        
            
                var html_aa197a7e0d657704aa843a2a8e711b67 = $(`<div id="html_aa197a7e0d657704aa843a2a8e711b67" style="width: 100.0%; height: 100.0%;">E M MARIO ALVES ARAUJO SILVA---</div>`)[0];
                popup_cf094fa14801604c77f89fdf6935e45f.setContent(html_aa197a7e0d657704aa843a2a8e711b67);
            
        

        marker_ad79d6ee20d766e849dd7c1b34580bdc.bindPopup(popup_cf094fa14801604c77f89fdf6935e45f)
        ;

        
    
    
            var marker_740083e48a6c93188ad86701bcb46bcf = L.marker(
                [-18.975452, -48.2669313],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_7d4584d8d4b24c7875443fe0ed2b69d2 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_740083e48a6c93188ad86701bcb46bcf.setIcon(icon_7d4584d8d4b24c7875443fe0ed2b69d2);
        
    
        var popup_0f42f3cad0216237406ef8f3b58ebbc3 = L.popup({"maxWidth": "100%"});

        
            
                var html_099ecbd580a5c0bf3ddac3f180ad6f32 = $(`<div id="html_099ecbd580a5c0bf3ddac3f180ad6f32" style="width: 100.0%; height: 100.0%;">ESCOLA MUNICIPAL DO BAIRRO SHOPPING PARK---</div>`)[0];
                popup_0f42f3cad0216237406ef8f3b58ebbc3.setContent(html_099ecbd580a5c0bf3ddac3f180ad6f32);
            
        

        marker_740083e48a6c93188ad86701bcb46bcf.bindPopup(popup_0f42f3cad0216237406ef8f3b58ebbc3)
        ;

        
    
    
            var marker_ca193ec33990c7be26c54522f28c31b7 = L.marker(
                [-18.962484, -48.2229477],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_aeba98f888fe3f4149e22c9d10dbffba = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_ca193ec33990c7be26c54522f28c31b7.setIcon(icon_aeba98f888fe3f4149e22c9d10dbffba);
        
    
        var popup_baab698d2e1b0eb9a7fccb7856b52228 = L.popup({"maxWidth": "100%"});

        
            
                var html_a37d46f7346354cb94d263f31466f990 = $(`<div id="html_a37d46f7346354cb94d263f31466f990" style="width: 100.0%; height: 100.0%;">E M ODILON CUSTODIO PEREIRA---</div>`)[0];
                popup_baab698d2e1b0eb9a7fccb7856b52228.setContent(html_a37d46f7346354cb94d263f31466f990);
            
        

        marker_ca193ec33990c7be26c54522f28c31b7.bindPopup(popup_baab698d2e1b0eb9a7fccb7856b52228)
        ;

        
    
    
            var marker_42070bd7bc16de53e1257216db302ac5 = L.marker(
                [-18.8660419, -48.2661153],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_c6a05fc8ed0fdcdf8804936b08233dfa = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_42070bd7bc16de53e1257216db302ac5.setIcon(icon_c6a05fc8ed0fdcdf8804936b08233dfa);
        
    
        var popup_955242e0a0d6f664efb12b1af4c8e299 = L.popup({"maxWidth": "100%"});

        
            
                var html_1172a17d26d303f792d844358f7e44f5 = $(`<div id="html_1172a17d26d303f792d844358f7e44f5" style="width: 100.0%; height: 100.0%;">E M PROFESSORA ORLANDA NEVES STRACK---</div>`)[0];
                popup_955242e0a0d6f664efb12b1af4c8e299.setContent(html_1172a17d26d303f792d844358f7e44f5);
            
        

        marker_42070bd7bc16de53e1257216db302ac5.bindPopup(popup_955242e0a0d6f664efb12b1af4c8e299)
        ;

        
    
    
            var marker_1c8e04eca6ef1f03fc826234f4bba685 = L.marker(
                [-18.9134042, -48.2071251],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_0026deaa534913116f5cf32f51c6ecad = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_1c8e04eca6ef1f03fc826234f4bba685.setIcon(icon_0026deaa534913116f5cf32f51c6ecad);
        
    
        var popup_94537f83836767e4252cc8603ef620a3 = L.popup({"maxWidth": "100%"});

        
            
                var html_d4c1a9e37da53f39c79072c96b4c7bcf = $(`<div id="html_d4c1a9e37da53f39c79072c96b4c7bcf" style="width: 100.0%; height: 100.0%;">EE PROFESSOR PAULO FREIRE---</div>`)[0];
                popup_94537f83836767e4252cc8603ef620a3.setContent(html_d4c1a9e37da53f39c79072c96b4c7bcf);
            
        

        marker_1c8e04eca6ef1f03fc826234f4bba685.bindPopup(popup_94537f83836767e4252cc8603ef620a3)
        ;

        
    
    
            var marker_c0a460604a191962c93596acf02ce8c5 = L.marker(
                [-18.8792599, -48.2323169],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_e9442ac247bf7b8cd3ce03fcf863e84c = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_c0a460604a191962c93596acf02ce8c5.setIcon(icon_e9442ac247bf7b8cd3ce03fcf863e84c);
        
    
        var popup_acc9787c8507d079f5d8071c2282a2f4 = L.popup({"maxWidth": "100%"});

        
            
                var html_094cdd77fba61acc52f208f42009a6ef = $(`<div id="html_094cdd77fba61acc52f208f42009a6ef" style="width: 100.0%; height: 100.0%;">EMEI RAIMUNDO VIEIRA DA CUNHA---</div>`)[0];
                popup_acc9787c8507d079f5d8071c2282a2f4.setContent(html_094cdd77fba61acc52f208f42009a6ef);
            
        

        marker_c0a460604a191962c93596acf02ce8c5.bindPopup(popup_acc9787c8507d079f5d8071c2282a2f4)
        ;

        
    
    
            var marker_2fd5207b0c92a814a1b5cf782fe47ad5 = L.marker(
                [-18.8870066, -48.2193163],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_dc2211c7ddd46696b2e2e7c08ee08b2f = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_2fd5207b0c92a814a1b5cf782fe47ad5.setIcon(icon_dc2211c7ddd46696b2e2e7c08ee08b2f);
        
    
        var popup_4f2b3fa18ef9f0f9654d999efd76ea88 = L.popup({"maxWidth": "100%"});

        
            
                var html_ce3279a5b6ebaa77bc0d90d1d793edb5 = $(`<div id="html_ce3279a5b6ebaa77bc0d90d1d793edb5" style="width: 100.0%; height: 100.0%;">EMEI CORA CORALINA---</div>`)[0];
                popup_4f2b3fa18ef9f0f9654d999efd76ea88.setContent(html_ce3279a5b6ebaa77bc0d90d1d793edb5);
            
        

        marker_2fd5207b0c92a814a1b5cf782fe47ad5.bindPopup(popup_4f2b3fa18ef9f0f9654d999efd76ea88)
        ;

        
    
    
            var marker_fd38c893f1c0ef46483708a87e1487e6 = L.marker(
                [-18.9367805, -48.2798078],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_47ffb9dd6c68d338edf9d2fd4be29e05 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_fd38c893f1c0ef46483708a87e1487e6.setIcon(icon_47ffb9dd6c68d338edf9d2fd4be29e05);
        
    
        var popup_d159126b5aa02089301f64709d5d454e = L.popup({"maxWidth": "100%"});

        
            
                var html_2411e0b9c6ac423c6e46a1396d08e3da = $(`<div id="html_2411e0b9c6ac423c6e46a1396d08e3da" style="width: 100.0%; height: 100.0%;">EMEI GRANDE OTELO---</div>`)[0];
                popup_d159126b5aa02089301f64709d5d454e.setContent(html_2411e0b9c6ac423c6e46a1396d08e3da);
            
        

        marker_fd38c893f1c0ef46483708a87e1487e6.bindPopup(popup_d159126b5aa02089301f64709d5d454e)
        ;

        
    
    
            var marker_573f676a439b7d358ec815c91d9ef525 = L.marker(
                [-18.9005546, -48.2838832],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_c4e3a9581bceffb2e8f349fbfcebbfee = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_573f676a439b7d358ec815c91d9ef525.setIcon(icon_c4e3a9581bceffb2e8f349fbfcebbfee);
        
    
        var popup_fbac3c5653d8cfc699959cb430b5a73d = L.popup({"maxWidth": "100%"});

        
            
                var html_6665267ee20dfa36e26f7c75bd618642 = $(`<div id="html_6665267ee20dfa36e26f7c75bd618642" style="width: 100.0%; height: 100.0%;">EMEI ROOSEVELT---</div>`)[0];
                popup_fbac3c5653d8cfc699959cb430b5a73d.setContent(html_6665267ee20dfa36e26f7c75bd618642);
            
        

        marker_573f676a439b7d358ec815c91d9ef525.bindPopup(popup_fbac3c5653d8cfc699959cb430b5a73d)
        ;

        
    
    
            var marker_fc4908e8ba4378f51cafc8747e351da6 = L.marker(
                [-18.8959132, -48.2377881],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_c18b9e3713ebfe3f6d488f31e1bd822a = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_fc4908e8ba4378f51cafc8747e351da6.setIcon(icon_c18b9e3713ebfe3f6d488f31e1bd822a);
        
    
        var popup_d530293db27ae12bf7be6b37b60adc7f = L.popup({"maxWidth": "100%"});

        
            
                var html_ecd64c4cf25db5354d758560b68fbee7 = $(`<div id="html_ecd64c4cf25db5354d758560b68fbee7" style="width: 100.0%; height: 100.0%;">EMEI MONTEIRO LOBATO---</div>`)[0];
                popup_d530293db27ae12bf7be6b37b60adc7f.setContent(html_ecd64c4cf25db5354d758560b68fbee7);
            
        

        marker_fc4908e8ba4378f51cafc8747e351da6.bindPopup(popup_d530293db27ae12bf7be6b37b60adc7f)
        ;

        
    
    
            var marker_2eb9ff12f44e3c2b5003d2c325e24873 = L.marker(
                [-18.9163003, -48.2465452],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_3eeeec03dd7b309495bc392604ee83be = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_2eb9ff12f44e3c2b5003d2c325e24873.setIcon(icon_3eeeec03dd7b309495bc392604ee83be);
        
    
        var popup_7e2d98cb15c7d1dffbe2de01d35ec404 = L.popup({"maxWidth": "100%"});

        
            
                var html_7ece4c96ea892099351a79b7eadca9ee = $(`<div id="html_7ece4c96ea892099351a79b7eadca9ee" style="width: 100.0%; height: 100.0%;">EMEI ZACARIAS PEREIRA DA SILVA---</div>`)[0];
                popup_7e2d98cb15c7d1dffbe2de01d35ec404.setContent(html_7ece4c96ea892099351a79b7eadca9ee);
            
        

        marker_2eb9ff12f44e3c2b5003d2c325e24873.bindPopup(popup_7e2d98cb15c7d1dffbe2de01d35ec404)
        ;

        
    
    
            var marker_1de2f2d3ae3ca107916f7c17884a903a = L.marker(
                [-18.9143763, -48.1958693],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_03ed89c1133e8100669d36abcaa19f95 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_1de2f2d3ae3ca107916f7c17884a903a.setIcon(icon_03ed89c1133e8100669d36abcaa19f95);
        
    
        var popup_fa239b0feb98de3eaedb9455410caa09 = L.popup({"maxWidth": "100%"});

        
            
                var html_704e78d8da5486f7e9ccb7e1682712f6 = $(`<div id="html_704e78d8da5486f7e9ccb7e1682712f6" style="width: 100.0%; height: 100.0%;">EMEI HIPOLITA TERESA ERANCI---</div>`)[0];
                popup_fa239b0feb98de3eaedb9455410caa09.setContent(html_704e78d8da5486f7e9ccb7e1682712f6);
            
        

        marker_1de2f2d3ae3ca107916f7c17884a903a.bindPopup(popup_fa239b0feb98de3eaedb9455410caa09)
        ;

        
    
    
            var marker_681603a98cf66bdaf71597c4e885370f = L.marker(
                [-18.9383041, -48.2993479],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_aeedb1de69d0815d635b46440eb392b2 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_681603a98cf66bdaf71597c4e885370f.setIcon(icon_aeedb1de69d0815d635b46440eb392b2);
        
    
        var popup_7772ba7a5ff95b4e17e629f85d31ae67 = L.popup({"maxWidth": "100%"});

        
            
                var html_4f98ab043f28c43ced4fb788a6a77351 = $(`<div id="html_4f98ab043f28c43ced4fb788a6a77351" style="width: 100.0%; height: 100.0%;">EMEI SAO FRANCISCO DE ASSIS---</div>`)[0];
                popup_7772ba7a5ff95b4e17e629f85d31ae67.setContent(html_4f98ab043f28c43ced4fb788a6a77351);
            
        

        marker_681603a98cf66bdaf71597c4e885370f.bindPopup(popup_7772ba7a5ff95b4e17e629f85d31ae67)
        ;

        
    
    
            var marker_9881cfca389a779f7458d7b0a551c4e6 = L.marker(
                [-18.9540209, -48.30382669999999],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_4f6012c40bbae4e1365785ff37c5cdd1 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_9881cfca389a779f7458d7b0a551c4e6.setIcon(icon_4f6012c40bbae4e1365785ff37c5cdd1);
        
    
        var popup_ce5ecb806ee33fd099f7e2d073e825b1 = L.popup({"maxWidth": "100%"});

        
            
                var html_3ee09011a1045f524662c25664b0f164 = $(`<div id="html_3ee09011a1045f524662c25664b0f164" style="width: 100.0%; height: 100.0%;">EMEI PROFª OLIVIA CALABRIA---</div>`)[0];
                popup_ce5ecb806ee33fd099f7e2d073e825b1.setContent(html_3ee09011a1045f524662c25664b0f164);
            
        

        marker_9881cfca389a779f7458d7b0a551c4e6.bindPopup(popup_ce5ecb806ee33fd099f7e2d073e825b1)
        ;

        
    
    
            var marker_6f7cf3dfc907ce8a0ab58a7682e9bc53 = L.marker(
                [-18.9298426, -48.24312339999999],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_a46340a4c4aa8d587adc274a6739da61 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_6f7cf3dfc907ce8a0ab58a7682e9bc53.setIcon(icon_a46340a4c4aa8d587adc274a6739da61);
        
    
        var popup_42a18a7a020ea7f759ec1c0d160e6b69 = L.popup({"maxWidth": "100%"});

        
            
                var html_522e2130911f6566617d5bc068ee8ddc = $(`<div id="html_522e2130911f6566617d5bc068ee8ddc" style="width: 100.0%; height: 100.0%;">EMEI PAMPULHA---</div>`)[0];
                popup_42a18a7a020ea7f759ec1c0d160e6b69.setContent(html_522e2130911f6566617d5bc068ee8ddc);
            
        

        marker_6f7cf3dfc907ce8a0ab58a7682e9bc53.bindPopup(popup_42a18a7a020ea7f759ec1c0d160e6b69)
        ;

        
    
    
            var marker_2ffb1ef4f85b8d379f5c73e733b00396 = L.marker(
                [-18.9293354, -48.2636689],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_cc852961ec179a58fedb16f8a615f403 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_2ffb1ef4f85b8d379f5c73e733b00396.setIcon(icon_cc852961ec179a58fedb16f8a615f403);
        
    
        var popup_c5e69d82fe6269ca71a98f35b28dd2fc = L.popup({"maxWidth": "100%"});

        
            
                var html_a852c14b3b3e37dedf90f0e551123664 = $(`<div id="html_a852c14b3b3e37dedf90f0e551123664" style="width: 100.0%; height: 100.0%;">EMEI PAULO FREIRE---</div>`)[0];
                popup_c5e69d82fe6269ca71a98f35b28dd2fc.setContent(html_a852c14b3b3e37dedf90f0e551123664);
            
        

        marker_2ffb1ef4f85b8d379f5c73e733b00396.bindPopup(popup_c5e69d82fe6269ca71a98f35b28dd2fc)
        ;

        
    
    
            var marker_693bde87d5820fec9eae0cf0e3eef52d = L.marker(
                [-18.9296057, -48.3109778],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_58f349cd91480eff859bfc8c9a1b2385 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_693bde87d5820fec9eae0cf0e3eef52d.setIcon(icon_58f349cd91480eff859bfc8c9a1b2385);
        
    
        var popup_1d8babac0c86dce4cd2346b912fa3e36 = L.popup({"maxWidth": "100%"});

        
            
                var html_cb21b2e9a2840bccf31a84d53219751e = $(`<div id="html_cb21b2e9a2840bccf31a84d53219751e" style="width: 100.0%; height: 100.0%;">EMEI PLANALTO---</div>`)[0];
                popup_1d8babac0c86dce4cd2346b912fa3e36.setContent(html_cb21b2e9a2840bccf31a84d53219751e);
            
        

        marker_693bde87d5820fec9eae0cf0e3eef52d.bindPopup(popup_1d8babac0c86dce4cd2346b912fa3e36)
        ;

        
    
    
            var marker_288ca0c53d011d73e4324663bb0c9a1f = L.marker(
                [-18.9160167, -48.328411],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_62bb35cf273fa7aac30106fa24ea3049 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_288ca0c53d011d73e4324663bb0c9a1f.setIcon(icon_62bb35cf273fa7aac30106fa24ea3049);
        
    
        var popup_fc444d5e1359045695a7692b76504928 = L.popup({"maxWidth": "100%"});

        
            
                var html_e72feb8a02bbfa3518107426e4c97398 = $(`<div id="html_e72feb8a02bbfa3518107426e4c97398" style="width: 100.0%; height: 100.0%;">EMEI PROFª IZILDINHA MARIA MACEDO DO AMARAL---</div>`)[0];
                popup_fc444d5e1359045695a7692b76504928.setContent(html_e72feb8a02bbfa3518107426e4c97398);
            
        

        marker_288ca0c53d011d73e4324663bb0c9a1f.bindPopup(popup_fc444d5e1359045695a7692b76504928)
        ;

        
    
    
            var marker_954aec0d1d6863364403fe1504e56ee6 = L.marker(
                [-18.8984026, -48.3051306],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_aa9751d23616ec9cd018c6c1a436a397 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_954aec0d1d6863364403fe1504e56ee6.setIcon(icon_aa9751d23616ec9cd018c6c1a436a397);
        
    
        var popup_9b5ef8fa2af5a43d6d935931fd2053f4 = L.popup({"maxWidth": "100%"});

        
            
                var html_5565695d9f8ba7da06457d551b5d7ba9 = $(`<div id="html_5565695d9f8ba7da06457d551b5d7ba9" style="width: 100.0%; height: 100.0%;">EMEI MARIA APARECIDA DA SILVA---</div>`)[0];
                popup_9b5ef8fa2af5a43d6d935931fd2053f4.setContent(html_5565695d9f8ba7da06457d551b5d7ba9);
            
        

        marker_954aec0d1d6863364403fe1504e56ee6.bindPopup(popup_9b5ef8fa2af5a43d6d935931fd2053f4)
        ;

        
    
    
            var marker_f953b70f9d7540d49ccecf78d805e1b1 = L.marker(
                [-18.9696836, -48.3251208],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_be5e50428d1b86aaf25dfb08898d6894 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_f953b70f9d7540d49ccecf78d805e1b1.setIcon(icon_be5e50428d1b86aaf25dfb08898d6894);
        
    
        var popup_1a18961b7992b2b3fca961c4a552086e = L.popup({"maxWidth": "100%"});

        
            
                var html_bb00607a91ea3cc3fdbf81b5f0dce52e = $(`<div id="html_bb00607a91ea3cc3fdbf81b5f0dce52e" style="width: 100.0%; height: 100.0%;">EM PROFESSORA JOSIANY FRANCA---</div>`)[0];
                popup_1a18961b7992b2b3fca961c4a552086e.setContent(html_bb00607a91ea3cc3fdbf81b5f0dce52e);
            
        

        marker_f953b70f9d7540d49ccecf78d805e1b1.bindPopup(popup_1a18961b7992b2b3fca961c4a552086e)
        ;

        
    
    
            var marker_46e72d9d87ff47181ff192322180724d = L.marker(
                [-18.9130934, -48.2038033],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_b65ae49d15770b61e67f0ab094a2b125 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_46e72d9d87ff47181ff192322180724d.setIcon(icon_b65ae49d15770b61e67f0ab094a2b125);
        
    
        var popup_c3bde63f30c4bfb57674a6517051a218 = L.popup({"maxWidth": "100%"});

        
            
                var html_3227d92f62b5940fef9f4b5e0625f0de = $(`<div id="html_3227d92f62b5940fef9f4b5e0625f0de" style="width: 100.0%; height: 100.0%;">EE DE ENSINO FUNDAMENTAL E MEDIO---</div>`)[0];
                popup_c3bde63f30c4bfb57674a6517051a218.setContent(html_3227d92f62b5940fef9f4b5e0625f0de);
            
        

        marker_46e72d9d87ff47181ff192322180724d.bindPopup(popup_c3bde63f30c4bfb57674a6517051a218)
        ;

        
    
    
            var marker_52a6e0677793e81dd819ec56e2966a11 = L.marker(
                [-18.9172367, -48.1975877],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_5bbe7006211eca4dd6ee4f8f3055c4e0 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_52a6e0677793e81dd819ec56e2966a11.setIcon(icon_5bbe7006211eca4dd6ee4f8f3055c4e0);
        
    
        var popup_a119cfbe0f76a82a155c241980601732 = L.popup({"maxWidth": "100%"});

        
            
                var html_a51fa75f10e31fadff57ffb85997fc36 = $(`<div id="html_a51fa75f10e31fadff57ffb85997fc36" style="width: 100.0%; height: 100.0%;">E M PROFª IRENE MONTEIRO JORGE---</div>`)[0];
                popup_a119cfbe0f76a82a155c241980601732.setContent(html_a51fa75f10e31fadff57ffb85997fc36);
            
        

        marker_52a6e0677793e81dd819ec56e2966a11.bindPopup(popup_a119cfbe0f76a82a155c241980601732)
        ;

        
    
    
            var marker_c499fbca5a15c60ff9e9eed517b8166a = L.marker(
                [-18.9247475, -48.2790589],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_b29f4b26b4ddedb8a4997ec8ff3590a4 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_c499fbca5a15c60ff9e9eed517b8166a.setIcon(icon_b29f4b26b4ddedb8a4997ec8ff3590a4);
        
    
        var popup_44ada93b9506552d92ac8b7f2f575ea1 = L.popup({"maxWidth": "100%"});

        
            
                var html_4cf8e2c0edb26a6ae04f12a4471ba69b = $(`<div id="html_4cf8e2c0edb26a6ae04f12a4471ba69b" style="width: 100.0%; height: 100.0%;">EMEI LIRIA EMILIA SARAIVA---</div>`)[0];
                popup_44ada93b9506552d92ac8b7f2f575ea1.setContent(html_4cf8e2c0edb26a6ae04f12a4471ba69b);
            
        

        marker_c499fbca5a15c60ff9e9eed517b8166a.bindPopup(popup_44ada93b9506552d92ac8b7f2f575ea1)
        ;

        
    
    
            var marker_2e73435084d807a46b7b14db21705fe1 = L.marker(
                [-18.8900531, -48.332305],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_89c48589fcb1ade3ce6b14ca37f2450f = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_2e73435084d807a46b7b14db21705fe1.setIcon(icon_89c48589fcb1ade3ce6b14ca37f2450f);
        
    
        var popup_12340d47e79476e3ab4f0fcc9e159fc8 = L.popup({"maxWidth": "100%"});

        
            
                var html_1a6fcb552ea9e0594a7937658570dbe7 = $(`<div id="html_1a6fcb552ea9e0594a7937658570dbe7" style="width: 100.0%; height: 100.0%;">EMEI DO BAIRRO GUARANI---</div>`)[0];
                popup_12340d47e79476e3ab4f0fcc9e159fc8.setContent(html_1a6fcb552ea9e0594a7937658570dbe7);
            
        

        marker_2e73435084d807a46b7b14db21705fe1.bindPopup(popup_12340d47e79476e3ab4f0fcc9e159fc8)
        ;

        
    
    
            var marker_32800b236a941584970e19f58f8c1371 = L.marker(
                [-18.9180955, -48.1856537],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_365413872ab6dc13ab1f6e4552c1f25f = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_32800b236a941584970e19f58f8c1371.setIcon(icon_365413872ab6dc13ab1f6e4552c1f25f);
        
    
        var popup_b5fd6235f30495df5ee63f3c79fda10e = L.popup({"maxWidth": "100%"});

        
            
                var html_f028458e61da33fe8d4de821647ecf6d = $(`<div id="html_f028458e61da33fe8d4de821647ecf6d" style="width: 100.0%; height: 100.0%;">EMEI ANISIO SPINOLA TEIXEIRA---</div>`)[0];
                popup_b5fd6235f30495df5ee63f3c79fda10e.setContent(html_f028458e61da33fe8d4de821647ecf6d);
            
        

        marker_32800b236a941584970e19f58f8c1371.bindPopup(popup_b5fd6235f30495df5ee63f3c79fda10e)
        ;

        
    
    
            var marker_37bb68e456be493230abccd804a080af = L.marker(
                [-18.9275047, -48.250414],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_8bf55235f4354869cafd201df5f94205 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_37bb68e456be493230abccd804a080af.setIcon(icon_8bf55235f4354869cafd201df5f94205);
        
    
        var popup_819ee6a3757b60d0c7d0020f994c136c = L.popup({"maxWidth": "100%"});

        
            
                var html_17873ae9acd55b6352c9de19deb1cdb5 = $(`<div id="html_17873ae9acd55b6352c9de19deb1cdb5" style="width: 100.0%; height: 100.0%;">EMEI PROFª GESIMEIRE FATIMA ARAUJO---</div>`)[0];
                popup_819ee6a3757b60d0c7d0020f994c136c.setContent(html_17873ae9acd55b6352c9de19deb1cdb5);
            
        

        marker_37bb68e456be493230abccd804a080af.bindPopup(popup_819ee6a3757b60d0c7d0020f994c136c)
        ;

        
    
    
            var marker_951efa586c9b5b432d85587721abc3bf = L.marker(
                [-18.9346006, -48.34367719999999],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_591c445f6d4bf5d546f6f8b5e3040ef9 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_951efa586c9b5b432d85587721abc3bf.setIcon(icon_591c445f6d4bf5d546f6f8b5e3040ef9);
        
    
        var popup_dcc3c9b888e4bdd569c5c9b2fe389604 = L.popup({"maxWidth": "100%"});

        
            
                var html_ffeeadb9273cc7b88bc34b3692747c6e = $(`<div id="html_ffeeadb9273cc7b88bc34b3692747c6e" style="width: 100.0%; height: 100.0%;">EMEI DO BAIRRO MANSOUR---</div>`)[0];
                popup_dcc3c9b888e4bdd569c5c9b2fe389604.setContent(html_ffeeadb9273cc7b88bc34b3692747c6e);
            
        

        marker_951efa586c9b5b432d85587721abc3bf.bindPopup(popup_dcc3c9b888e4bdd569c5c9b2fe389604)
        ;

        
    
    
            var marker_9336799ca7596b5130c3fde6a0b1db11 = L.marker(
                [-18.9082646, -48.2119332],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_f87806f14985a6bf17197bfa32c76527 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_9336799ca7596b5130c3fde6a0b1db11.setIcon(icon_f87806f14985a6bf17197bfa32c76527);
        
    
        var popup_b9ecd1f077bc301057e9c611142547ba = L.popup({"maxWidth": "100%"});

        
            
                var html_0f4d3c9dded9647e6c9a1e144b47c488 = $(`<div id="html_0f4d3c9dded9647e6c9a1e144b47c488" style="width: 100.0%; height: 100.0%;">EMEI DO BAIRRO DOM ALMIR---</div>`)[0];
                popup_b9ecd1f077bc301057e9c611142547ba.setContent(html_0f4d3c9dded9647e6c9a1e144b47c488);
            
        

        marker_9336799ca7596b5130c3fde6a0b1db11.bindPopup(popup_b9ecd1f077bc301057e9c611142547ba)
        ;

        
    
    
            var marker_67607db384b39c177b0c4663973e6ea2 = L.marker(
                [-18.9122093, -48.2705687],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_21b40c51ba84cf90d8f1db1478295f10 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_67607db384b39c177b0c4663973e6ea2.setIcon(icon_21b40c51ba84cf90d8f1db1478295f10);
        
    
        var popup_c38435fc369f223de4f87c622e3a81a9 = L.popup({"maxWidth": "100%"});

        
            
                var html_7b9ea3480d644ebd3b6a1530bf173960 = $(`<div id="html_7b9ea3480d644ebd3b6a1530bf173960" style="width: 100.0%; height: 100.0%;">EMEI DO BAIRRO APARECIDA---</div>`)[0];
                popup_c38435fc369f223de4f87c622e3a81a9.setContent(html_7b9ea3480d644ebd3b6a1530bf173960);
            
        

        marker_67607db384b39c177b0c4663973e6ea2.bindPopup(popup_c38435fc369f223de4f87c622e3a81a9)
        ;

        
    
    
            var marker_98020ff3a239be9c7eda4cac57bb028f = L.marker(
                [-18.8697127, -48.2861156],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_bc72c3a4c358f51c2466818ba1bba152 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_98020ff3a239be9c7eda4cac57bb028f.setIcon(icon_bc72c3a4c358f51c2466818ba1bba152);
        
    
        var popup_bbca604415452c0da37bac8592b58b53 = L.popup({"maxWidth": "100%"});

        
            
                var html_2902a2d5b3f038666195526eb13341e6 = $(`<div id="html_2902a2d5b3f038666195526eb13341e6" style="width: 100.0%; height: 100.0%;">EMEI DO BAIRRO CRUZEIRO DO SUL---</div>`)[0];
                popup_bbca604415452c0da37bac8592b58b53.setContent(html_2902a2d5b3f038666195526eb13341e6);
            
        

        marker_98020ff3a239be9c7eda4cac57bb028f.bindPopup(popup_bbca604415452c0da37bac8592b58b53)
        ;

        
    
    
            var marker_f0ba8d0a14b325b41709708b3f6b666a = L.marker(
                [-18.8769172, -48.2794383],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_999ae1924ea00937cf287eaeda358497 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_f0ba8d0a14b325b41709708b3f6b666a.setIcon(icon_999ae1924ea00937cf287eaeda358497);
        
    
        var popup_14059c15054fe2c38da7210a1cdd32ad = L.popup({"maxWidth": "100%"});

        
            
                var html_eded1a412992b9a6938f7520ea5766d1 = $(`<div id="html_eded1a412992b9a6938f7520ea5766d1" style="width: 100.0%; height: 100.0%;">EMEI DO BAIRRO ESPERANCA---</div>`)[0];
                popup_14059c15054fe2c38da7210a1cdd32ad.setContent(html_eded1a412992b9a6938f7520ea5766d1);
            
        

        marker_f0ba8d0a14b325b41709708b3f6b666a.bindPopup(popup_14059c15054fe2c38da7210a1cdd32ad)
        ;

        
    
    
            var marker_10ae2ecda7dea6d32ebaa5ef6a87617a = L.marker(
                [-18.8862961, -48.2728153],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_1830816f42cc887cf562888da5ada60c = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_10ae2ecda7dea6d32ebaa5ef6a87617a.setIcon(icon_1830816f42cc887cf562888da5ada60c);
        
    
        var popup_f7a2273c148977d0247d251082501c53 = L.popup({"maxWidth": "100%"});

        
            
                var html_bd7fcb59a2cbf5f68873a882f6babb29 = $(`<div id="html_bd7fcb59a2cbf5f68873a882f6babb29" style="width: 100.0%; height: 100.0%;">EMEI DO BAIRRO MARTA HELENA---</div>`)[0];
                popup_f7a2273c148977d0247d251082501c53.setContent(html_bd7fcb59a2cbf5f68873a882f6babb29);
            
        

        marker_10ae2ecda7dea6d32ebaa5ef6a87617a.bindPopup(popup_f7a2273c148977d0247d251082501c53)
        ;

        
    
    
            var marker_3ba0cc2151e675581b8d82af86881ce6 = L.marker(
                [-18.8691948, -48.28024550000001],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_eaef633b285d81a605e7c768085ae22d = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_3ba0cc2151e675581b8d82af86881ce6.setIcon(icon_eaef633b285d81a605e7c768085ae22d);
        
    
        var popup_ec22cbdb54a1d13d12785ef3aa692786 = L.popup({"maxWidth": "100%"});

        
            
                var html_820cbda3b90755095d7476553ae36fdf = $(`<div id="html_820cbda3b90755095d7476553ae36fdf" style="width: 100.0%; height: 100.0%;">EMEI DO BAIRRO NOSSA SENHORA DAS GRACAS---</div>`)[0];
                popup_ec22cbdb54a1d13d12785ef3aa692786.setContent(html_820cbda3b90755095d7476553ae36fdf);
            
        

        marker_3ba0cc2151e675581b8d82af86881ce6.bindPopup(popup_ec22cbdb54a1d13d12785ef3aa692786)
        ;

        
    
    
            var marker_7a9b2f59f61d4de64218617b029760cc = L.marker(
                [-18.9364414, -48.279837],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_f8e6efc175c028f98c2b07c08fb8cd03 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_7a9b2f59f61d4de64218617b029760cc.setIcon(icon_f8e6efc175c028f98c2b07c08fb8cd03);
        
    
        var popup_fe6b09d8ae179658f845cac1694ae54e = L.popup({"maxWidth": "100%"});

        
            
                var html_28655e1f3ee962c32feeb7a2fd385126 = $(`<div id="html_28655e1f3ee962c32feeb7a2fd385126" style="width: 100.0%; height: 100.0%;">EMEI DO BAIRRO PATRIMONIO I---</div>`)[0];
                popup_fe6b09d8ae179658f845cac1694ae54e.setContent(html_28655e1f3ee962c32feeb7a2fd385126);
            
        

        marker_7a9b2f59f61d4de64218617b029760cc.bindPopup(popup_fe6b09d8ae179658f845cac1694ae54e)
        ;

        
    
    
            var marker_84c8da61532aa38ae2aeac7a211bfea8 = L.marker(
                [-18.9435832, -48.2438334],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_6febff9bb6c0db56a542fdd8a058e1fb = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_84c8da61532aa38ae2aeac7a211bfea8.setIcon(icon_6febff9bb6c0db56a542fdd8a058e1fb);
        
    
        var popup_ee4001ea5744103a4c2dd5b008b6e1cb = L.popup({"maxWidth": "100%"});

        
            
                var html_5cf161a3d80d913f3643e19a2c73b2a8 = $(`<div id="html_5cf161a3d80d913f3643e19a2c73b2a8" style="width: 100.0%; height: 100.0%;">EMEI DO BAIRRO SANTA LUZIA---</div>`)[0];
                popup_ee4001ea5744103a4c2dd5b008b6e1cb.setContent(html_5cf161a3d80d913f3643e19a2c73b2a8);
            
        

        marker_84c8da61532aa38ae2aeac7a211bfea8.bindPopup(popup_ee4001ea5744103a4c2dd5b008b6e1cb)
        ;

        
    
    
            var marker_3cca0ac0d041975bf463074b3efb4c68 = L.marker(
                [-18.9326043, -48.2296737],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_46775af737138523d8aa4d2ff51563e7 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_3cca0ac0d041975bf463074b3efb4c68.setIcon(icon_46775af737138523d8aa4d2ff51563e7);
        
    
        var popup_0abde018a6b68a72b274745f70a5bdd5 = L.popup({"maxWidth": "100%"});

        
            
                var html_b8770e7fcf09ac943064333abe13c127 = $(`<div id="html_b8770e7fcf09ac943064333abe13c127" style="width: 100.0%; height: 100.0%;">EMEI PROFª CORNELIA YARA CASTANHEIRA---</div>`)[0];
                popup_0abde018a6b68a72b274745f70a5bdd5.setContent(html_b8770e7fcf09ac943064333abe13c127);
            
        

        marker_3cca0ac0d041975bf463074b3efb4c68.bindPopup(popup_0abde018a6b68a72b274745f70a5bdd5)
        ;

        
    
    
            var marker_c7741b95ed4713c87a4bda42a2169274 = L.marker(
                [-18.8997737, -48.2486448],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_9d84d051f6881801d60e9b6885392f29 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_c7741b95ed4713c87a4bda42a2169274.setIcon(icon_9d84d051f6881801d60e9b6885392f29);
        
    
        var popup_349799be8a888072537daf557798b06c = L.popup({"maxWidth": "100%"});

        
            
                var html_ad636e3b7ba5a8562c3139df1b620987 = $(`<div id="html_ad636e3b7ba5a8562c3139df1b620987" style="width: 100.0%; height: 100.0%;">EMEI DO BAIRRO TIBERY---</div>`)[0];
                popup_349799be8a888072537daf557798b06c.setContent(html_ad636e3b7ba5a8562c3139df1b620987);
            
        

        marker_c7741b95ed4713c87a4bda42a2169274.bindPopup(popup_349799be8a888072537daf557798b06c)
        ;

        
    
    
            var marker_c8e40ba03cce6e95869db5f98752328c = L.marker(
                [-18.8983086, -48.3385572],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_d2f312dbbca41bdd77f3a289cc866d51 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_c8e40ba03cce6e95869db5f98752328c.setIcon(icon_d2f312dbbca41bdd77f3a289cc866d51);
        
    
        var popup_31089f0910adf9aefac3c25fc3b3fde5 = L.popup({"maxWidth": "100%"});

        
            
                var html_0de4bc66597f5a79798885ed5752500b = $(`<div id="html_0de4bc66597f5a79798885ed5752500b" style="width: 100.0%; height: 100.0%;">EMEI DO BAIRRO TOCANTINS---</div>`)[0];
                popup_31089f0910adf9aefac3c25fc3b3fde5.setContent(html_0de4bc66597f5a79798885ed5752500b);
            
        

        marker_c8e40ba03cce6e95869db5f98752328c.bindPopup(popup_31089f0910adf9aefac3c25fc3b3fde5)
        ;

        
    
    
            var marker_faa691151b924cd7439803e5c7cb1e01 = L.marker(
                [-18.8869925, -48.2979694],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_e10889a5aa9b2a063d45a675c0080aea = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_faa691151b924cd7439803e5c7cb1e01.setIcon(icon_e10889a5aa9b2a063d45a675c0080aea);
        
    
        var popup_c436e6b045e78f0099ea2fd9df2ca5cb = L.popup({"maxWidth": "100%"});

        
            
                var html_62c3251f9912ca6ffb69035901016ab5 = $(`<div id="html_62c3251f9912ca6ffb69035901016ab5" style="width: 100.0%; height: 100.0%;">EMEI FRANCISCO BUENO MONTEIRO---</div>`)[0];
                popup_c436e6b045e78f0099ea2fd9df2ca5cb.setContent(html_62c3251f9912ca6ffb69035901016ab5);
            
        

        marker_faa691151b924cd7439803e5c7cb1e01.bindPopup(popup_c436e6b045e78f0099ea2fd9df2ca5cb)
        ;

        
    
    
            var marker_b1ddfa0f1cb61cfc3970c3e69e9e7f9b = L.marker(
                [-18.9221705, -48.2009188],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_6f2e3c1889b1a500c2e0aac52033ea33 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_b1ddfa0f1cb61cfc3970c3e69e9e7f9b.setIcon(icon_6f2e3c1889b1a500c2e0aac52033ea33);
        
    
        var popup_01d74938f260f2416c1c41a4cc086e25 = L.popup({"maxWidth": "100%"});

        
            
                var html_adce0445dbd9cd1a5b89944f8f69d105 = $(`<div id="html_adce0445dbd9cd1a5b89944f8f69d105" style="width: 100.0%; height: 100.0%;">EMEI MARIA TEREZINHA CUNHA SILVA---</div>`)[0];
                popup_01d74938f260f2416c1c41a4cc086e25.setContent(html_adce0445dbd9cd1a5b89944f8f69d105);
            
        

        marker_b1ddfa0f1cb61cfc3970c3e69e9e7f9b.bindPopup(popup_01d74938f260f2416c1c41a4cc086e25)
        ;

        
    
    
            var marker_7f4004d5fd97093f468ff0d75213f29f = L.marker(
                [-18.9192225, -48.2889024],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_5b1b24da778138e262fe50a1399c2790 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_7f4004d5fd97093f468ff0d75213f29f.setIcon(icon_5b1b24da778138e262fe50a1399c2790);
        
    
        var popup_3aadbe72a796452a0b0d29c05d26a41c = L.popup({"maxWidth": "100%"});

        
            
                var html_28dfff69b59587f0c6e88ad9fd21f4b6 = $(`<div id="html_28dfff69b59587f0c6e88ad9fd21f4b6" style="width: 100.0%; height: 100.0%;">EMEI DO BAIRRO MARTINS---</div>`)[0];
                popup_3aadbe72a796452a0b0d29c05d26a41c.setContent(html_28dfff69b59587f0c6e88ad9fd21f4b6);
            
        

        marker_7f4004d5fd97093f468ff0d75213f29f.bindPopup(popup_3aadbe72a796452a0b0d29c05d26a41c)
        ;

        
    
    
            var marker_5a73a37b07c096ba1ccf3fedfa3d39ce = L.marker(
                [-18.9349441, -48.30378779999999],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_6947fb3c642d97395fa4b007363e3dda = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_5a73a37b07c096ba1ccf3fedfa3d39ce.setIcon(icon_6947fb3c642d97395fa4b007363e3dda);
        
    
        var popup_0bb50848ace24b2fb15b31c570aa7397 = L.popup({"maxWidth": "100%"});

        
            
                var html_eb8dcd1eea7c5a456fd84888ac352b62 = $(`<div id="html_eb8dcd1eea7c5a456fd84888ac352b62" style="width: 100.0%; height: 100.0%;">EMEI DO BAIRRO TUBALINA---</div>`)[0];
                popup_0bb50848ace24b2fb15b31c570aa7397.setContent(html_eb8dcd1eea7c5a456fd84888ac352b62);
            
        

        marker_5a73a37b07c096ba1ccf3fedfa3d39ce.bindPopup(popup_0bb50848ace24b2fb15b31c570aa7397)
        ;

        
    
    
            var marker_27b32855e20820c182390293a720b381 = L.marker(
                [-18.914147, -48.293533],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_6c781225ea5a59b1638510c77ebb89e3 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_27b32855e20820c182390293a720b381.setIcon(icon_6c781225ea5a59b1638510c77ebb89e3);
        
    
        var popup_2ded75ea9fe2fcf7a08754d2e4aafd85 = L.popup({"maxWidth": "100%"});

        
            
                var html_c79da7924107d05d9561fd605829038f = $(`<div id="html_c79da7924107d05d9561fd605829038f" style="width: 100.0%; height: 100.0%;">EMEI VERA ANITA NASCIMENTO DE SOUZA---</div>`)[0];
                popup_2ded75ea9fe2fcf7a08754d2e4aafd85.setContent(html_c79da7924107d05d9561fd605829038f);
            
        

        marker_27b32855e20820c182390293a720b381.bindPopup(popup_2ded75ea9fe2fcf7a08754d2e4aafd85)
        ;

        
    
    
            var marker_6176be0d5562262fb285b8988aa72b51 = L.marker(
                [-18.904164, -48.3176455],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_9c268371ea0a3891e9750fcc52e9932b = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_6176be0d5562262fb285b8988aa72b51.setIcon(icon_9c268371ea0a3891e9750fcc52e9932b);
        
    
        var popup_5b6888df31b62e13e5b3be9492ce749a = L.popup({"maxWidth": "100%"});

        
            
                var html_393d5a9e37d5c99c7e243650cf88b279 = $(`<div id="html_393d5a9e37d5c99c7e243650cf88b279" style="width: 100.0%; height: 100.0%;">EMEI JEAN PIAGET---</div>`)[0];
                popup_5b6888df31b62e13e5b3be9492ce749a.setContent(html_393d5a9e37d5c99c7e243650cf88b279);
            
        

        marker_6176be0d5562262fb285b8988aa72b51.bindPopup(popup_5b6888df31b62e13e5b3be9492ce749a)
        ;

        
    
    
            var marker_b858736747808b5c5b315270013b75b8 = L.marker(
                [-18.8911141, -48.2433766],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_068747f1a48e9739b06997d5cb013375 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_b858736747808b5c5b315270013b75b8.setIcon(icon_068747f1a48e9739b06997d5cb013375);
        
    
        var popup_3542ae58082fd411498306c58472cd2a = L.popup({"maxWidth": "100%"});

        
            
                var html_9116e229c8301d5a5e19bc9e15b67cc0 = $(`<div id="html_9116e229c8301d5a5e19bc9e15b67cc0" style="width: 100.0%; height: 100.0%;">EMEI DO BAIRRO CUSTODIO PEREIRA---</div>`)[0];
                popup_3542ae58082fd411498306c58472cd2a.setContent(html_9116e229c8301d5a5e19bc9e15b67cc0);
            
        

        marker_b858736747808b5c5b315270013b75b8.bindPopup(popup_3542ae58082fd411498306c58472cd2a)
        ;

        
    
    
            var marker_b6a1dfd249595727f42fc6bb2730c3da = L.marker(
                [-18.9612967, -48.2197827],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_e017ec11042942ae24bbf36861b1453a = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_b6a1dfd249595727f42fc6bb2730c3da.setIcon(icon_e017ec11042942ae24bbf36861b1453a);
        
    
        var popup_e2805d59e554d0b6fd626ed77746fe1f = L.popup({"maxWidth": "100%"});

        
            
                var html_8e7f012a1d66195407bef4f36743cad4 = $(`<div id="html_8e7f012a1d66195407bef4f36743cad4" style="width: 100.0%; height: 100.0%;">EMEI AUGUSTA MARIA DE FREITAS---</div>`)[0];
                popup_e2805d59e554d0b6fd626ed77746fe1f.setContent(html_8e7f012a1d66195407bef4f36743cad4);
            
        

        marker_b6a1dfd249595727f42fc6bb2730c3da.bindPopup(popup_e2805d59e554d0b6fd626ed77746fe1f)
        ;

        
    
    
            var marker_479174e655d02d7f4a6c4793eaeb98c6 = L.marker(
                [-18.9127749, -48.2755227],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_df26e1c55d4385b420e3fe2aac0153b7 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_479174e655d02d7f4a6c4793eaeb98c6.setIcon(icon_df26e1c55d4385b420e3fe2aac0153b7);
        
    
        var popup_51dcd547332e8299ed510fc867874461 = L.popup({"maxWidth": "100%"});

        
            
                var html_24b0f934f41f470567077de4bd5fc66a = $(`<div id="html_24b0f934f41f470567077de4bd5fc66a" style="width: 100.0%; height: 100.0%;">ESCOLA MUNICIPAL IRMA ODELCIA LEAO CARNEIRO---</div>`)[0];
                popup_51dcd547332e8299ed510fc867874461.setContent(html_24b0f934f41f470567077de4bd5fc66a);
            
        

        marker_479174e655d02d7f4a6c4793eaeb98c6.bindPopup(popup_51dcd547332e8299ed510fc867874461)
        ;

        
    
    
            var marker_58ba3701388acfe4fa7d49e9616b16b9 = L.marker(
                [-18.9142451, -48.322927],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_691b064eac1fbe9c2db81c2fe0e662e0 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_58ba3701388acfe4fa7d49e9616b16b9.setIcon(icon_691b064eac1fbe9c2db81c2fe0e662e0);
        
    
        var popup_ec7cd0ffbd8b77a73e285f1e2c0ccebc = L.popup({"maxWidth": "100%"});

        
            
                var html_c3b373da905e347c421111001b596ca4 = $(`<div id="html_c3b373da905e347c421111001b596ca4" style="width: 100.0%; height: 100.0%;">EM INSPETORA FRANCE ABADIA MACHADO SANTANA---</div>`)[0];
                popup_ec7cd0ffbd8b77a73e285f1e2c0ccebc.setContent(html_c3b373da905e347c421111001b596ca4);
            
        

        marker_58ba3701388acfe4fa7d49e9616b16b9.bindPopup(popup_ec7cd0ffbd8b77a73e285f1e2c0ccebc)
        ;

        
    
    
            var marker_dfbde539368b4e8240b1cb8aa6587129 = L.marker(
                [-18.9552472, -48.3464343],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_46208738e2e67a7828e5d4c6229ff1ae = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_dfbde539368b4e8240b1cb8aa6587129.setIcon(icon_46208738e2e67a7828e5d4c6229ff1ae);
        
    
        var popup_386be6feccce0639f296f67dbc5692c7 = L.popup({"maxWidth": "100%"});

        
            
                var html_484452d205458991f1050718d0037d29 = $(`<div id="html_484452d205458991f1050718d0037d29" style="width: 100.0%; height: 100.0%;">EMEI JORNALISTA LUIZ FERNANDO QUIRINO---</div>`)[0];
                popup_386be6feccce0639f296f67dbc5692c7.setContent(html_484452d205458991f1050718d0037d29);
            
        

        marker_dfbde539368b4e8240b1cb8aa6587129.bindPopup(popup_386be6feccce0639f296f67dbc5692c7)
        ;

        
    
    
            var marker_d4b659258111437103f953d5bbbada18 = L.marker(
                [-18.9046818, -48.31961159999999],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_aa6459aabed3295c23e5e3b732d5d591 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_d4b659258111437103f953d5bbbada18.setIcon(icon_aa6459aabed3295c23e5e3b732d5d591);
        
    
        var popup_b5967791a28471ca5086a41240f3de3c = L.popup({"maxWidth": "100%"});

        
            
                var html_224c54e2cce5ac23167df85efed626be = $(`<div id="html_224c54e2cce5ac23167df85efed626be" style="width: 100.0%; height: 100.0%;">EMEI PROFª ELOAH MARISA DE MENEZES---</div>`)[0];
                popup_b5967791a28471ca5086a41240f3de3c.setContent(html_224c54e2cce5ac23167df85efed626be);
            
        

        marker_d4b659258111437103f953d5bbbada18.bindPopup(popup_b5967791a28471ca5086a41240f3de3c)
        ;

        
    
    
            var marker_9f61a8734c6763650715d7c41356f846 = L.marker(
                [-18.9284187, -48.33485580000001],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_44a6ba8ad97eb37c84389f4e64045516 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_9f61a8734c6763650715d7c41356f846.setIcon(icon_44a6ba8ad97eb37c84389f4e64045516);
        
    
        var popup_5d8feee12e5abe222cfecd01cd6a39f1 = L.popup({"maxWidth": "100%"});

        
            
                var html_11a8b21f40b8a7153a11321526c8bac7 = $(`<div id="html_11a8b21f40b8a7153a11321526c8bac7" style="width: 100.0%; height: 100.0%;">EMEI PROFª SONIA APARECIDA ALVARES DE OLIVEIRA---</div>`)[0];
                popup_5d8feee12e5abe222cfecd01cd6a39f1.setContent(html_11a8b21f40b8a7153a11321526c8bac7);
            
        

        marker_9f61a8734c6763650715d7c41356f846.bindPopup(popup_5d8feee12e5abe222cfecd01cd6a39f1)
        ;

        
    
    
            var marker_ccbe214d6da2d644234824e6bd227d4d = L.marker(
                [-18.9881275, -48.2665442],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_e77eca261608ca5a407706b3dfdc7ea5 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_ccbe214d6da2d644234824e6bd227d4d.setIcon(icon_e77eca261608ca5a407706b3dfdc7ea5);
        
    
        var popup_58185708072df0e79343433067668883 = L.popup({"maxWidth": "100%"});

        
            
                var html_1425fa738c4dbdbbbb27b137a71142c1 = $(`<div id="html_1425fa738c4dbdbbbb27b137a71142c1" style="width: 100.0%; height: 100.0%;">EMEI DO BAIRRO SHOPPING PARK---</div>`)[0];
                popup_58185708072df0e79343433067668883.setContent(html_1425fa738c4dbdbbbb27b137a71142c1);
            
        

        marker_ccbe214d6da2d644234824e6bd227d4d.bindPopup(popup_58185708072df0e79343433067668883)
        ;

        
    
    
            var marker_733695e9affce09acb9073c5a91341d7 = L.marker(
                [-18.9667547, -48.2206765],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_4db9c7f2cbd1086bacf599621c09f475 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_733695e9affce09acb9073c5a91341d7.setIcon(icon_4db9c7f2cbd1086bacf599621c09f475);
        
    
        var popup_34e2410f50822f00b1f17601a9c7ac48 = L.popup({"maxWidth": "100%"});

        
            
                var html_24f3f4e69b7477b3ec59856539057934 = $(`<div id="html_24f3f4e69b7477b3ec59856539057934" style="width: 100.0%; height: 100.0%;">EMEI PROFª ROSANGELA BORGES CUNHA---</div>`)[0];
                popup_34e2410f50822f00b1f17601a9c7ac48.setContent(html_24f3f4e69b7477b3ec59856539057934);
            
        

        marker_733695e9affce09acb9073c5a91341d7.bindPopup(popup_34e2410f50822f00b1f17601a9c7ac48)
        ;

        
    
    
            var marker_c9c5d3515b55e4b045f08e9008200615 = L.marker(
                [-18.9554207, -48.3464232],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_e8d85c4f783842fb6c2ba9282460265c = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_c9c5d3515b55e4b045f08e9008200615.setIcon(icon_e8d85c4f783842fb6c2ba9282460265c);
        
    
        var popup_e7dff9356096f5252b157c0319821e6c = L.popup({"maxWidth": "100%"});

        
            
                var html_b2543a7b169b1b4d1950c2ad13feba10 = $(`<div id="html_b2543a7b169b1b4d1950c2ad13feba10" style="width: 100.0%; height: 100.0%;">ESCOLA MUNICIPAL PROFESSORA CARLOTA DE ANDRADE MARQUEZ---</div>`)[0];
                popup_e7dff9356096f5252b157c0319821e6c.setContent(html_b2543a7b169b1b4d1950c2ad13feba10);
            
        

        marker_c9c5d3515b55e4b045f08e9008200615.bindPopup(popup_e7dff9356096f5252b157c0319821e6c)
        ;

        
    
    
            var marker_079563014bb9f9fffdca92f90195025d = L.marker(
                [-18.9882981, -48.2672065],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_d5888bc1eed016b63c522506a0947fb0 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_079563014bb9f9fffdca92f90195025d.setIcon(icon_d5888bc1eed016b63c522506a0947fb0);
        
    
        var popup_1524cff71d839c7d40051f4beb0a0440 = L.popup({"maxWidth": "100%"});

        
            
                var html_701134133434f10d9c17f22e8492bb3f = $(`<div id="html_701134133434f10d9c17f22e8492bb3f" style="width: 100.0%; height: 100.0%;">PRESIDENTE ITAMAR FRANCO---</div>`)[0];
                popup_1524cff71d839c7d40051f4beb0a0440.setContent(html_701134133434f10d9c17f22e8492bb3f);
            
        

        marker_079563014bb9f9fffdca92f90195025d.bindPopup(popup_1524cff71d839c7d40051f4beb0a0440)
        ;

        
    
    
            var marker_d51d984fb24a3f748c975ddcfbfcb9d6 = L.marker(
                [-18.9640456, -48.3197396],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_e4590a2020340bba1124e5df7cde9ce1 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_d51d984fb24a3f748c975ddcfbfcb9d6.setIcon(icon_e4590a2020340bba1124e5df7cde9ce1);
        
    
        var popup_5e44e515a828f306a3f4c2ad008d132b = L.popup({"maxWidth": "100%"});

        
            
                var html_ee8995ad9eef3f1d43c30137d3e0a4fe = $(`<div id="html_ee8995ad9eef3f1d43c30137d3e0a4fe" style="width: 100.0%; height: 100.0%;">CENTRO SOLIDARIO DE EDUCACAO INFANTIL DE UBERLANDIA---</div>`)[0];
                popup_5e44e515a828f306a3f4c2ad008d132b.setContent(html_ee8995ad9eef3f1d43c30137d3e0a4fe);
            
        

        marker_d51d984fb24a3f748c975ddcfbfcb9d6.bindPopup(popup_5e44e515a828f306a3f4c2ad008d132b)
        ;

        
    
    
            var marker_e22d69a636a1a463795b871290c15d28 = L.marker(
                [-18.8955671, -48.2836641],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_428d35057d104f2eec489f851032bba6 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_e22d69a636a1a463795b871290c15d28.setIcon(icon_428d35057d104f2eec489f851032bba6);
        
    
        var popup_382ffc791a9092cf22ead40c39fcdcde = L.popup({"maxWidth": "100%"});

        
            
                var html_73a0472259b51dc542f4d392e80c5e70 = $(`<div id="html_73a0472259b51dc542f4d392e80c5e70" style="width: 100.0%; height: 100.0%;">EMEI EURIPEDES ROCHA---</div>`)[0];
                popup_382ffc791a9092cf22ead40c39fcdcde.setContent(html_73a0472259b51dc542f4d392e80c5e70);
            
        

        marker_e22d69a636a1a463795b871290c15d28.bindPopup(popup_382ffc791a9092cf22ead40c39fcdcde)
        ;

        
    
    
            var marker_54ce76ce7f9d7ed2cf4d5d474c4b2d03 = L.marker(
                [-18.88345, -48.2840972],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_2b7b2e5ce9734b9673b46522bedf4907 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_54ce76ce7f9d7ed2cf4d5d474c4b2d03.setIcon(icon_2b7b2e5ce9734b9673b46522bedf4907);
        
    
        var popup_516a60deae8ab7a5b9337f3f30f93991 = L.popup({"maxWidth": "100%"});

        
            
                var html_ecf3401dafa47275f703ce2d9e1ce5d3 = $(`<div id="html_ecf3401dafa47275f703ce2d9e1ce5d3" style="width: 100.0%; height: 100.0%;">EMEI PROF SERGIO APARECIDO DA SILVA---</div>`)[0];
                popup_516a60deae8ab7a5b9337f3f30f93991.setContent(html_ecf3401dafa47275f703ce2d9e1ce5d3);
            
        

        marker_54ce76ce7f9d7ed2cf4d5d474c4b2d03.bindPopup(popup_516a60deae8ab7a5b9337f3f30f93991)
        ;

        
    
    
            var marker_52b3f489be8315313e28b1838d6e98f3 = L.marker(
                [-18.9218125, -48.2658941],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_20c2ec2fe0738b9ed64fb0f9e76ce26d = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_52b3f489be8315313e28b1838d6e98f3.setIcon(icon_20c2ec2fe0738b9ed64fb0f9e76ce26d);
        
    
        var popup_7ca008ce8a3ea548b1a4824a8fb8fa6f = L.popup({"maxWidth": "100%"});

        
            
                var html_24352bbada56c8909514b569b48321b7 = $(`<div id="html_24352bbada56c8909514b569b48321b7" style="width: 100.0%; height: 100.0%;">COLEGIO TIRADENTES PMMG---</div>`)[0];
                popup_7ca008ce8a3ea548b1a4824a8fb8fa6f.setContent(html_24352bbada56c8909514b569b48321b7);
            
        

        marker_52b3f489be8315313e28b1838d6e98f3.bindPopup(popup_7ca008ce8a3ea548b1a4824a8fb8fa6f)
        ;

        
    
    
            var marker_07c61c3b59652e9501fcde9a780e0607 = L.marker(
                [-18.9114012, -48.2533108],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_21a7621007fd3dfe065b3048ec34cdde = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_07c61c3b59652e9501fcde9a780e0607.setIcon(icon_21a7621007fd3dfe065b3048ec34cdde);
        
    
        var popup_77424da7a15993b6626a63d8706c190c = L.popup({"maxWidth": "100%"});

        
            
                var html_8b5dcfd546fd0679f143dbd4d97256b0 = $(`<div id="html_8b5dcfd546fd0679f143dbd4d97256b0" style="width: 100.0%; height: 100.0%;">EMEI PROFª SHIRLEY LOURDES DE MENEZES VIEIRA---</div>`)[0];
                popup_77424da7a15993b6626a63d8706c190c.setContent(html_8b5dcfd546fd0679f143dbd4d97256b0);
            
        

        marker_07c61c3b59652e9501fcde9a780e0607.bindPopup(popup_77424da7a15993b6626a63d8706c190c)
        ;

        
    
    
            var marker_fbf6b33c6226b6140b4a641f5bba98ff = L.marker(
                [-18.9197932, -48.3333759],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_41a7d37a56275b9277f335238eafc5a6 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_fbf6b33c6226b6140b4a641f5bba98ff.setIcon(icon_41a7d37a56275b9277f335238eafc5a6);
        
    
        var popup_c1dfa9a41b672b3808932b0750a6aedb = L.popup({"maxWidth": "100%"});

        
            
                var html_28efa6a9ca1af2004e5114d0999202b9 = $(`<div id="html_28efa6a9ca1af2004e5114d0999202b9" style="width: 100.0%; height: 100.0%;">EMEI MARIA FLORIPES ALVES---</div>`)[0];
                popup_c1dfa9a41b672b3808932b0750a6aedb.setContent(html_28efa6a9ca1af2004e5114d0999202b9);
            
        

        marker_fbf6b33c6226b6140b4a641f5bba98ff.bindPopup(popup_c1dfa9a41b672b3808932b0750a6aedb)
        ;

        
    
    
            var marker_249d984ee13a458184a4b547ce862ef4 = L.marker(
                [-18.9598547, -48.3126626],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_52acda0bb1fea37b8ab907e0fe0045b7 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_249d984ee13a458184a4b547ce862ef4.setIcon(icon_52acda0bb1fea37b8ab907e0fe0045b7);
        
    
        var popup_f02b48abb8bc7240441a867aa5f466c5 = L.popup({"maxWidth": "100%"});

        
            
                var html_4f4b1dfa632f22d2ab535e9f9ad02676 = $(`<div id="html_4f4b1dfa632f22d2ab535e9f9ad02676" style="width: 100.0%; height: 100.0%;">EMEI PROFESSORA CLESILDA ALVES ROSA---</div>`)[0];
                popup_f02b48abb8bc7240441a867aa5f466c5.setContent(html_4f4b1dfa632f22d2ab535e9f9ad02676);
            
        

        marker_249d984ee13a458184a4b547ce862ef4.bindPopup(popup_f02b48abb8bc7240441a867aa5f466c5)
        ;

        
    
    
            var marker_82df5f4f751bb346e86075a8d6f4f7c3 = L.marker(
                [-18.9290682, -48.3306237],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_552ad4e0945a5b5cbb21e3d8eedf8353 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_82df5f4f751bb346e86075a8d6f4f7c3.setIcon(icon_552ad4e0945a5b5cbb21e3d8eedf8353);
        
    
        var popup_52652a5a075bfa702397db19a3c07d73 = L.popup({"maxWidth": "100%"});

        
            
                var html_c1f35c6b09caa844f6fcc3e49b04f68e = $(`<div id="html_c1f35c6b09caa844f6fcc3e49b04f68e" style="width: 100.0%; height: 100.0%;">EMEI PROFª VERIDIANA RODRIGUES CARNEIRO---</div>`)[0];
                popup_52652a5a075bfa702397db19a3c07d73.setContent(html_c1f35c6b09caa844f6fcc3e49b04f68e);
            
        

        marker_82df5f4f751bb346e86075a8d6f4f7c3.bindPopup(popup_52652a5a075bfa702397db19a3c07d73)
        ;

        
    
    
            var marker_4f4b1cc644dd46023134fbad584d85ac = L.marker(
                [-18.9281853, -48.330358],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_411a2d109e0ab654d45b8b4290e455ad = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_4f4b1cc644dd46023134fbad584d85ac.setIcon(icon_411a2d109e0ab654d45b8b4290e455ad);
        
    
        var popup_6a25bfd594db91f60e642ecb43e31b80 = L.popup({"maxWidth": "100%"});

        
            
                var html_3943d74d99f019b323decf88ddefa8ed = $(`<div id="html_3943d74d99f019b323decf88ddefa8ed" style="width: 100.0%; height: 100.0%;">E M PROF VALDIR ARAUJO---</div>`)[0];
                popup_6a25bfd594db91f60e642ecb43e31b80.setContent(html_3943d74d99f019b323decf88ddefa8ed);
            
        

        marker_4f4b1cc644dd46023134fbad584d85ac.bindPopup(popup_6a25bfd594db91f60e642ecb43e31b80)
        ;

        
    
    
            var marker_4e9d0a69cae7076f8d88ec0ab258ae55 = L.marker(
                [-18.9208066, -48.2256118],
                {}
            ).addTo(map_b6fd6ebc617c1509ca1a4ffb4cc2df85);
        
    
            var icon_42211b1875a56024a6fcd968ac1da471 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "school", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_4e9d0a69cae7076f8d88ec0ab258ae55.setIcon(icon_42211b1875a56024a6fcd968ac1da471);
        
    
        var popup_60f480637857f954777f736302916e16 = L.popup({"maxWidth": "100%"});

        
            
                var html_84fd9667917c6e606e1bddf9c66e0534 = $(`<div id="html_84fd9667917c6e606e1bddf9c66e0534" style="width: 100.0%; height: 100.0%;">E M ESTUDANTE MIRELLY FERNANDES SOUZA---</div>`)[0];
                popup_60f480637857f954777f736302916e16.setContent(html_84fd9667917c6e606e1bddf9c66e0534);
            
        

        marker_4e9d0a69cae7076f8d88ec0ab258ae55.bindPopup(popup_60f480637857f954777f736302916e16)
        ;

        
    
</script>
</div> 
