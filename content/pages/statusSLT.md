Title: Status SLT
Date: 2024-07-12 14:25
Author: Michael Ring
SortOrder: 200
Stylesheets: overridestyles.css lightgallery.css
## Clear Sky Chart Starfront Observatories
<p style="width:1024px;">
<a href=https://www.cleardarksky.com/c/StrfrntObsTXkey.html>
<img src="https://www.cleardarksky.com/c/StrfrntObsTXcsk.gif?c=2012437"></a>
</p>
## Liveview
<p style="width:1024px;">
<table>
  <thead>
    <tr>
      <th width="33%">Last Image</th>
      <th width="33%">Pier Camera</th>
      <th width="33%">Building Camera</th>
    <tr>
  </thead>
  <tbody>
    <tr id="tr-td">
      <td data-src="https://slt-observatory.space/images/slt-images/subimage.jpg">
        <img src="https://slt-observatory.space/images/slt-images/subimage.jpg"/>
      </td>
      <td data-src="https://slt-observatory.space/images/slt-images/image.jpg">
        <img src="https://slt-observatory.space/images/slt-images/image.jpg"/>
      </td>
      <td data-src="https://zyssufjepmbhqznfuwcw.supabase.co/storage/v1/object/public/status-assets-public/building-0005/allsky/images/image.jpg">
        <img src="https://zyssufjepmbhqznfuwcw.supabase.co/storage/v1/object/public/status-assets-public/building-0005/allsky/images/image.jpg"/>
      </td>
    </tr>
  </tbody>
</table>
<table>
  <thead>
    <tr>
      <th width="33%">NOAA CloudCoverage</th>
      <th width="33%">NOAA Radar</th>
      <th width="33%">AllSky</th>
    <tr>
  </thead>
  <tbody>
    <tr id="tr-td2">
      <td data-src="https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/sp/GEOCOLOR/GOES16-SP-GEOCOLOR-600x600.gif">
        <img src="https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/sp/GEOCOLOR/GOES16-SP-GEOCOLOR-600x600.gif"/>
      </td>
      <td data-src="https://radar.weather.gov/ridge/standard/KSJT_loop.gif">
        <img src="https://radar.weather.gov/ridge/standard/KSJT_loop.gif"/>
      </td>

      <td data-src="https://slt-observatory.space/images/starfront-allsky/allsky.webp">
        <img src="https://slt-observatory.space/images/starfront-allsky/allsky-thumb.webp"/>
      </td>
    </tr>
  </tbody>
</table>
</p>
<!-- include status-slt.schedulerStatus.include -->
<!-- include status-slt.roofStatus.include -->
<!-- include status-slt.powerBoxStatus.include -->
<!-- include status-slt.skyAlertStatus.include -->
<!-- include status-slt.imageStatus.include -->
<script>
  lightGallery(document.getElementById('tr-td'));
  lightGallery(document.getElementById('tr-td2'));
  lightGallery(document.getElementById('selector'),{selector:'.sub',});
  lightGallery(document.getElementById('selector'),{selector:'.allsky',});
</script>
