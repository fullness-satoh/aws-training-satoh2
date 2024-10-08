# AWS研修用語集

## Section 1: EC2
- **サーバー**: クライアントからのリクエストを処理するコンピュータシステム。
- **EC2**: Amazonの仮想サーバーサービス。Elastic Compute Cloudの略。
- **リージョン**: AWSのデータセンターの地理的な場所。
- **OS**: オペレーティングシステム。サーバーの基本ソフトウェア。
- **Linux**: オープンソースのOS。多くのサーバーで利用される。
- **CPU**: Central Processing Unitの略で、コンピュータの「頭脳」として機能し、プログラムを実行するための基本的な計算処理を行うハードウェア。
- **vCPU**: 仮想CPU。物理CPUを仮想的に分割して使用するユニット。
- **メモリ**: データを一時的に保存するためのハードウェアリソース。
- **キーペア（秘密鍵・公開鍵）**: SSH接続に使用される認証方式のための鍵ペア。
- **RSA**: 公開鍵暗号方式の一種で、SSH接続で使用されることが多い。
- **SSH**: Secure Shellの略。リモートサーバーに安全に接続するためのプロトコル。
- **HTTPS・HTTP**: ウェブ通信のプロトコル。HTTPSは暗号化された通信。
- **ストレージ**: データを保存するための物理的な装置や仮想リソース。
- **IPv4**: インターネットプロトコルバージョン4。IPアドレスの一種。
- **パブリック IPv4**: インターネット上でアクセス可能なIPv4アドレス。
- **パブリック IPv4 DNS**: パブリックIPv4に関連付けられたDNS名。
- **chmod 600**: ファイルのパーミッションを設定するコマンド。ファイルを所有者だけが読み書きできるように設定。
- **セキュリティグループ**: インスタンスへのインバウンド/アウトバウンドトラフィックを制御するファイアウォールの役割。
- **AMI (Amazon Machine Image)**: EC2インスタンスのベースとなるイメージ。

## Section 2: デプロイ
- **ミドルウェア**: アプリケーションとOSの間で動作するソフトウェア（例: Webサーバー、データベース）。
- **ウェブサーバー**: クライアントにウェブページを提供するサーバーソフトウェア。
- **Nginx**: 高速でスケーラブルなWebサーバーとリバースプロキシ。
- **ポート番号**: 特定のアプリケーションに対応する通信チャネルを指定する番号。
- **sudo コマンド**: システム管理者権限でコマンドを実行するためのコマンド。
- **yum コマンド**: Red Hat系Linuxディストリビューションのパッケージ管理システム。
- **Dockerデーモン**: コンテナを管理・実行するためのバックグラウンドプロセス。
- **curl コマンド**: データを送受信するためのコマンドラインツール。
- **Gunicorn**: Pythonアプリケーション用のWSGI HTTPサーバー。
- **systemctl**: サービス管理のためのコマンド。

## Section 3: ドメイン設定
- **ドメイン**: インターネット上での特定の場所を指し示す名前（例: example.com）。
- **Route53**: AmazonのDNSサービス。ドメイン名とIPアドレスを対応付ける。
- **サブドメイン**: ドメインの一部として追加された名前（例: sub.example.com）。
- **ホストゾーン**: DNSレコードを管理するためのRoute53のコンテナ。
- **レコード**: ドメイン名とIPアドレスを対応付ける設定。
- **DNS (Domain Name System)**: ドメイン名とIPアドレスを対応付けるシステム。
- **TTL (Time to Live)**: DNSレコードのキャッシュの有効期間。

## Section 4: Debugモード解除
- **環境変数**: ソフトウェアの挙動を制御するためのシステム設定変数。
- **settings.py**: Djangoアプリケーションの設定ファイル。
- **ALLOWED_HOSTS**: 許可されたホストのリスト。

## Section 5: IAMとS3
- **S3**: AWSのオブジェクトストレージサービス。無限にスケーラブルなデータストレージ。
- **IAM**: Identity and Access Managementの略。AWSリソースへのアクセスを管理。
- **ロール**: IAMで定義されたアクセス権限のセット。特定のアクションにアクセス許可を与える。
- **グループ**: 複数のIAMユーザーをまとめて管理するための単位。
- **ポリシー**: IAMリソースに対してアクセス権を定義する文書。
- **バケット**: S3におけるデータストレージの単位。
- **ACL (Access Control List)**: S3バケットやオブジェクトのアクセス制御設定。

## その他
- **SSL**: Secure Sockets Layerの略。インターネット上でデータを暗号化して送信するプロトコル。
- **サブネット**: VPC内のIPアドレス範囲の一部。ネットワークのセグメント。
- **インターネットゲートウェイ**: VPCをインターネットに接続するための仮想装置。
- **VPC**: Virtual Private Cloudの略。仮想ネットワーク環境。
