QApplication: PyQt5 uygulamasını başlatır ve etkinleştirir. Uygulama döngüsünü yönetir.
QMainWindow: Ana pencereyi oluşturur. Bu sınıf, genellikle bir uygulamanın ana penceresini temsil eder.
QWidget: Kullanıcı arayüzünde bir bileşeni (widget) temsil eder. Ana pencere ve diğer bileşenler (butonlar, etiketler vb.) QWidget sınıfından türetilir.
QVBoxLayout ve QHBoxLayout: Dikey ve yatay düzenler oluşturmak için kullanılır. QVBoxLayout, bileşenleri dikey olarak düzenlerken, QHBoxLayout yatay olarak düzenler.
QLabel: Metin veya resim gibi bir içeriği görüntüler. Genellikle bir etiket olarak kullanılır.
QLineEdit: Metin girişi almak için kullanılır. Kullanıcıdan veri almak için kullanılır.
QPushButton: Tıklanabilir bir düğme oluşturur. Kullanıcı etkileşimleri için kullanılır.
QAction: Menüler, araç çubukları ve kısayol tuşları için eylemler tanımlar.
QMenuBar: Bir menü çubuğu oluşturur. Menüler, menü öğeleri ve alt menüler içerebilir.
QMenu: Menü öğelerini içeren bir menü oluşturur. Menü öğeleri, eylemleri veya alt menüleri temsil eder.
QMessageBox: Kullanıcıya mesaj kutuları göstermek için kullanılır. Bilgi, uyarı veya hata mesajları görüntülenebilir.
QCheckBox: Seçeneklerin işaretlenebileceği veya işaretinin kaldırılabileceği bir onay kutusu oluşturur.
QListWidget: Liste öğelerini göstermek için kullanılır. Kullanıcıların bir öğeyi seçmelerine izin verir.
QFont: Metinlerin görüntülenme şeklini ve boyutunu kontrol eder.
--------------------------
MAİNWİNDOW
initializeUI(): PyQt5 araçlarını kullanarak ana pencerenin arayüzünü oluşturur. Ana menü barı, butonlar ve diğer arayüz öğeleri burada tanımlanır.
display_home(): Ana sayfa görünümünü gösterir. Film ve dizi listelerini gösteren butonları, kullanıcı bilgilerini gösteren butonu görünür kılar.
display_user_info(): Kullanıcının bilgilerini içeren bir iletişim kutusu görüntüler.
display_watched_series(): Kullanıcının izlediği dizileri içeren bir iletişim kutusu görüntüler.
display_watched_movies(): Kullanıcının izlediği filmleri içeren bir iletişim kutusu görüntüler.
display_movies(): Film listesini gösterir. Her film için bir etiket ve "İzle" düğmesi oluşturur.
display_series(): Dizi listesini gösterir. Her dizi için bir etiket ve "İzle" düğmesi oluşturur.
watch_series(series): Bir dizi izlendiğinde bu metod çağrılır. İzlenen diziyi bir listeye ekler ve bir iletişim kutusu gösterir.
watch_movie(movie): Bir film izlendiğinde bu metod çağrılır. İzlenen filmi bir listeye ekler ve bir iletişim kutusu gösterir.
update_watched_series_widget(): İzlenen diziler listesini günceller.
update_watched_movies_widget(): İzlenen filmler listesini günceller.
hide_home_buttons(): Ana penceredeki butonları gizler ve "Ana Sayfa Dön" butonunu gösterir.
back_to_main_window(): Ana sayfaya döner.
-----------------------------
login window
initializeUI(): Kullanıcı arayüzünü oluşturur. Kullanıcı adı ve şifre için metin girişi, giriş düğmesi oluşturur.
check_credentials(): Kullanıcının giriş bilgilerini kontrol eder. Doğru giriş yapılırsa ana pencereyi gösterir.
-----------------------------
series widget ( dizi)
initializeUI(): Dizi listesi için arayüzü oluşturur.
watch_series(series): Bir dizi izlendiğinde bu metod çağrılır.
-----------------------------
movie widget ( film)
initializeUI(): Film listesi için arayüzü oluşturur.
watch_movie(movie): Bir film izlendiğinde bu metod çağrılır.
----------------------------------------------------------------------------------------------------------------------
 İlk olarak, giriş penceresini oluşturarak başladım. Kullanıcı "maruf" ve "korkutata" şeklinde doğru bilgileri girerse, ana pencereyi gösterir.
 Aksi takdirde, kullanıcıyı hatalı girişle ilgili uyarır. Bu kontrol, check_credentials() fonksiyonunda gerçekleşiyor.
Ana pencere, ana menü barı ve birkaç düğme içerir. Ana menü barı, kullanıcının bilgilerini görmesine ve izlediği dizileri veya 
filmleri kontrol etmesine izin verir. Ana penceredeki düğmeler, film ve dizi listelerini gösterir.
Dizi ve film listeleri, her bir öğe için bir etiket ve "İzle" düğmesi içerir. "İzle" düğmesine tıklandığında, ilgili dizi veya film izlenmiş listesine eklenir. 
İlgili fonksiyonlar, "İzle" düğmesine bağlanırken watch_series(series) ve watch_movie(movie) fonksiyonlarıdır.
Kullanıcı, menüden "İzlediğim Diziler" veya "İzlediğim Filmler" seçeneğini tıklayarak izlediği dizileri veya filmleri kontrol edebilir. Bu seçenekler, 
display_watched_series() ve display_watched_movies() fonksiyonlarında gerçekleşir. Eğer kullanıcı hiçbir dizi veya film izlemediyse, bir uyarı mesajı görünür.
Ayrıca, kullanıcı bilgilerini de görebilir. Bu bilgiler, "Kullanıcı Bilgileri" seçeneği tıklanarak alınır ve display_user_info() fonksiyonu tarafından görüntülenir.
Ana penceredeki "Anasayfa Dön" düğmesine tıklandığında, kullanıcı ana ekrana geri döner. Bu, back_to_main_window() fonksiyonunda gerçekleşir.
