# Definisikan keyword linguistic untuk masing-masing kategori usia
linguistic_keywords_18_24 = list(set([
    'anjay', 'wkwk', 'cie', 'gaje', 'gabut', 'mager', 'nongki', 'kepo', 'lebay', 'gila lu', 'yaelah',
    'santuy', 'caper', 'bucin', 'panik ga sih', 'receh', 'ciyee', 'baper', 'ngab', 'ngopi', 'ngabers',
    'fomo', 'flexing', 'healing', 'self-reward', 'auto', 'bestie', 'lo', 'gue', 'btw', 'OOTD', 'OOTN',
    'nolep', 'halu', 'cihuy', 'canda', 'goks', 'mantul', 'syantik', 'demen', 'alay', 'skuy', 'gaskeun',
    'ngablu', 'ngegas', 'pansos', 'julid', 'ngeri', 'ngakak', 'ngenes', 'sabi', 'eaaa', 'apasi',
    'woles', 'cuan', 'nyinyir', 'emang iya', 'kzl', 'idk', 'bruh', 'okey sip', 'ya kan', 'loh', 'lah',
    'lho', 'haha', 'hihi', 'hehe', 'wakaka', 'cuy', 'bro', 'sis', 'bray', 'woke', 'keknya', 'yahud',
    'sekut', 'slebew', 'emesh', 'gemay', 'pede', 'pd banget', 'rempong', 'ngaret', 'cocoklogi',
    'mabar', 'kepo banget', 'ga ngerti', 'ga jelas', 'sok iye', 'lebai', 'basi', 'kudet', 'kekinian',
    'peka', 'php', 'modus', 'bodo amat', 'udah lah', 'gatau', 'susah move on', 'galau', 'curhat',
    'ngehits', 'baperan', 'sobat', 'tante', 'om', 'belagu', 'brb', 'chill', 'vibes', 'squad', 'clout',
    'seru', 'tiktok', 'woke', 'ngecengin', 'heboh', 'marah-marah', 'tante-tante', 'om-om', 'sange', 
    'gaul', 'sosmed', 'vlog', 'tik-tok', 'gengs', 'ngaku', 'ngehits', 'baper banget', 'WTF', 'YOLO', 'LOL',
    'ROFL', 'DM', 'FFS', 'BRB', 'IDK', 'SMH', 'LMAO', 'TGIF', 'OOTD', 'BFF', 'LMK'
]))

linguistic_keywords_25_34 = list(set([
    'kerja', 'gaji', 'karir', 'pernikahan', 'cicilan', 'keluarga', 'anjir', 'santai', 'adulting', 'stress',
    'deadline', 'self-improvement', 'motivasi', 'self-care', 'ngobrol', 'recharge', 'health', 'balance',
    'conquer', 'empowerment', 'capek', 'nabung', 'budaya kerja', 'monthly', 'freedom', 'hustle', 'fokus',
    'rekreasi', 'productivity', 'pindah kantor', 'financial freedom', 'beberapa hal', 'donasi', 'generasi milenial',
    'achieve', 'work-life balance', 'investasi', 'prioritas', 'family time', 'pertemanan', 'career growth',
    'tanggung jawab', 'stress management', 'parenting', 'mama muda', 'papa muda', 'suami', 'istri', 'keuangan keluarga',
    'produktif', 'liburan bareng', 'traveling', 'gadget', 'teknologi', 'generasi 90an', 'rejeki nomplok', 'beli rumah',
    'kebutuhan anak', 'kehidupan baru', 'married life', 'rumah tangga', 'financial planning',
    'LDR', 'FOMO', 'TMI', 'GM', 'YOLO', 'VLOG', 'IRL', 'TBT', 'BTS', 'BFF', 'LMK', 'BRB', 'GMB', 'PR'
]))

linguistic_keywords_35_44 = list(set([
    'dengan ini', 'berdasarkan', 'diharapkan', 'kepada', 'menginformasikan', 'pengumuman', 'work-life harmony',
    'perusahaan', 'pencapaian', 'karir', 'mencapai tujuan', 'pendidikan', 'keluarga', 'berinvestasi', 'menabung',
    'keuangan', 'renovasi', 'rumah', 'pendidikan anak', 'pensiun', 'sehat', 'bekerja', 'cicilan rumah', 'gaji besar',
    'tabungan', 'liburan', 'kenyamanan', 'perjalanan hidup', 'rencana keuangan', 'perubahan hidup', 'refleksi',
    'tantangan', 'kemandirian', 'pemikiran jangka panjang', 'produk keuangan', 'generasi x', 'kehidupan profesional',
    'anak sekolah', 'pekerjaan kantor', 'pensiun dini', 'penghasilan tambahan', 'perjalanan karir', 'konsultasi keuangan',
    'guru', 'pendidikan anak', 'kesehatan jantung', 'rencana tabungan', 'liburan keluarga',
    'LMAO', 'TMI', 'TBH', 'HR', 'B2B', 'TMI', 'CEO', 'LDR', 'OOTD', 'CTO', 'FP'
]))

linguistic_keywords_45_54 = list(set([
    'bpjs', 'pensiun', 'jantung', 'asam urat', 'diabetes', 'keluarga', 'hidup sehat', 'perawatan', 'refleksi diri',
    'kesehatan', 'resep', 'prihatin', 'mental health', 'pendidikan lanjut', 'keuangan pensiun', 'perjalanan hidup',
    'penerimaan', 'kebahagiaan', 'tanggung jawab', 'komunitas', 'hobi', 'persahabatan', 'kenangan', 'diabetes', 
    'perawatan tubuh', 'evaluasi hidup', 'manajemen stres', 'investasi pensiun', 'generasi baby boomer', 'tabungan pensiun',
    'bekerja lebih lambat', 'cerita hidup', 'persiapan pensiun', 'penurunan energi', 'keamanan finansial', 'perawatan keluarga',
    'tenaga kesehatan', 'perawatan medis', 'kursus profesional', 'sosialisasi', 'teman-teman dekat',
    'ITB', 'CEO', 'ITR', 'FOMO', 'FB', 'B2B'
]))

linguistic_keywords_55_plus = list(set([
    'reminiscing', 'senja', 'pensiun', 'keluarga besar', 'kenangan', 'seru', 'liburan', 'cucunya', 'rekreasi',
    'jalan-jalan', 'refleksi kehidupan', 'kesederhanaan', 'pelajaran hidup', 'aktivitas sosial', 'kehidupan lebih tenang',
    'navigasi kehidupan', 'pemikiran jangka panjang', 'perawatan medis', 'lansia', 'hobi baru', 'pembelajaran',
    'kesadaran diri', 'relaksasi', 'energi positif', 'kesehatan mental', 'waktu sendiri', 'tidur siang', 'self-care',
    'kegiatan komunitas', 'senam pagi', 'berbagi pengalaman', 'perawatan kesehatan', 'CO', 'CMM', 'TL',
    'waktu keluarga', 'nanti aja', 'santai', 'pensiun bahagia', 'kesehatan', 'rehat', 'dengan tenang', 'kenangan',
    'liburan keluarga', 'grandchildren', 'pekerjaan terakhir', 'kehidupan sederhana', 'menikmati waktu', 'beristirahat',
    'fokus kesehatan', 'pensiun', 'generasi tua', 'menyusun warisan', 'senang-senang', 'baca buku', 'jalan-jalan santai',
    'makanan sehat', 'taman', 'jalan-jalan sore', 'cerita nostalgia', 'berbagi kebahagiaan', 'perawatan pribadi', 'renungan',
    'berkebun', 'donasi', 'mendukung anak cucu', 'lepas pensiun', 'rumah nyaman', 'BFF', 'COB', 'DRS', 'DP'
]))
