class EMsg:
	Invalid = 0
	Multi = 1
	BaseGeneral = 100
	GenericReply = 100
	DestJobFailed = 113
	Alert = 115
	SCIDRequest = 120
	SCIDResponse = 121
	JobHeartbeat = 123
	HubConnect = 124
	Subscribe = 126
	RouteMessage = 127
	RemoteSysID = 128
	AMCreateAccountResponse = 129
	WGRequest = 130
	WGResponse = 131
	KeepAlive = 132
	WebAPIJobRequest = 133
	WebAPIJobResponse = 134
	ClientSessionStart = 135
	ClientSessionEnd = 136
	ClientSessionUpdateAuthTicket = 137
	StatsDeprecated = 138
	Ping = 139
	PingResponse = 140
	Stats = 141
	RequestFullStatsBlock = 142
	LoadDBOCacheItem = 143
	LoadDBOCacheItemResponse = 144
	InvalidateDBOCacheItems = 145
	ServiceMethod = 146
	ServiceMethodResponse = 147
	BaseShell = 200
	AssignSysID = 200
	Exit = 201
	DirRequest = 202
	DirResponse = 203
	ZipRequest = 204
	ZipResponse = 205
	UpdateRecordResponse = 215
	UpdateCreditCardRequest = 221
	UpdateUserBanResponse = 225
	PrepareToExit = 226
	ContentDescriptionUpdate = 227
	TestResetServer = 228
	UniverseChanged = 229
	ShellConfigInfoUpdate = 230
	RequestWindowsEventLogEntries = 233
	ProvideWindowsEventLogEntries = 234
	ShellSearchLogs = 235
	ShellSearchLogsResponse = 236
	ShellCheckWindowsUpdates = 237
	ShellCheckWindowsUpdatesResponse = 238
	ShellFlushUserLicenseCache = 239
	BaseGM = 300
	Heartbeat = 300
	ShellFailed = 301
	ExitShells = 307
	ExitShell = 308
	GracefulExitShell = 309
	NotifyWatchdog = 314
	LicenseProcessingComplete = 316
	SetTestFlag = 317
	QueuedEmailsComplete = 318
	GMReportPHPError = 319
	GMDRMSync = 320
	PhysicalBoxInventory = 321
	UpdateConfigFile = 322
	TestInitDB = 323
	GMWriteConfigToSQL = 324
	GMLoadActivationCodes = 325
	GMQueueForFBS = 326
	GMSchemaConversionResults = 327
	GMSchemaConversionResultsResponse = 328
	GMWriteShellFailureToSQL = 329
	BaseAIS = 400
	AISRefreshContentDescription = 401
	AISRequestContentDescription = 402
	AISUpdateAppInfo = 403
	AISUpdatePackageInfo = 404
	AISGetPackageChangeNumber = 405
	AISGetPackageChangeNumberResponse = 406
	AISAppInfoTableChanged = 407
	AISUpdatePackageInfoResponse = 408
	AISCreateMarketingMessage = 409
	AISCreateMarketingMessageResponse = 410
	AISGetMarketingMessage = 411
	AISGetMarketingMessageResponse = 412
	AISUpdateMarketingMessage = 413
	AISUpdateMarketingMessageResponse = 414
	AISRequestMarketingMessageUpdate = 415
	AISDeleteMarketingMessage = 416
	AISGetMarketingTreatments = 419
	AISGetMarketingTreatmentsResponse = 420
	AISRequestMarketingTreatmentUpdate = 421
	AISTestAddPackage = 422
	AIGetAppGCFlags = 423
	AIGetAppGCFlagsResponse = 424
	AIGetAppList = 425
	AIGetAppListResponse = 426
	AIGetAppInfo = 427
	AIGetAppInfoResponse = 428
	AISGetCouponDefinition = 429
	AISGetCouponDefinitionResponse = 430
	BaseAM = 500
	AMUpdateUserBanRequest = 504
	AMAddLicense = 505
	AMBeginProcessingLicenses = 507
	AMSendSystemIMToUser = 508
	AMExtendLicense = 509
	AMAddMinutesToLicense = 510
	AMCancelLicense = 511
	AMInitPurchase = 512
	AMPurchaseResponse = 513
	AMGetFinalPrice = 514
	AMGetFinalPriceResponse = 515
	AMGetLegacyGameKey = 516
	AMGetLegacyGameKeyResponse = 517
	AMFindHungTransactions = 518
	AMSetAccountTrustedRequest = 519
	AMCompletePurchase = 521
	AMCancelPurchase = 522
	AMNewChallenge = 523
	AMFixPendingPurchase = 526
	AMIsUserBanned = 527
	AMRegisterKey = 528
	AMLoadActivationCodes = 529
	AMLoadActivationCodesResponse = 530
	AMLookupKeyResponse = 531
	AMLookupKey = 532
	AMChatCleanup = 533
	AMClanCleanup = 534
	AMFixPendingRefund = 535
	AMReverseChargeback = 536
	AMReverseChargebackResponse = 537
	AMClanCleanupList = 538
	AMGetLicenses = 539
	AMGetLicensesResponse = 540
	AllowUserToPlayQuery = 550
	AllowUserToPlayResponse = 551
	AMVerfiyUser = 552
	AMClientNotPlaying = 553
	ClientRequestFriendship = 554
	AMRelayPublishStatus = 555
	AMResetCommunityContent = 556
	AMPrimePersonaStateCache = 557
	AMAllowUserContentQuery = 558
	AMAllowUserContentResponse = 559
	AMInitPurchaseResponse = 560
	AMRevokePurchaseResponse = 561
	AMLockProfile = 562
	AMRefreshGuestPasses = 563
	AMInviteUserToClan = 564
	AMAcknowledgeClanInvite = 565
	AMGrantGuestPasses = 566
	AMClanDataUpdated = 567
	AMReloadAccount = 568
	AMClientChatMsgRelay = 569
	AMChatMulti = 570
	AMClientChatInviteRelay = 571
	AMChatInvite = 572
	AMClientJoinChatRelay = 573
	AMClientChatMemberInfoRelay = 574
	AMPublishChatMemberInfo = 575
	AMClientAcceptFriendInvite = 576
	AMChatEnter = 577
	AMClientPublishRemovalFromSource = 578
	AMChatActionResult = 579
	AMFindAccounts = 580
	AMFindAccountsResponse = 581
	AMSetAccountFlags = 584
	AMCreateClan = 586
	AMCreateClanResponse = 587
	AMGetClanDetails = 588
	AMGetClanDetailsResponse = 589
	AMSetPersonaName = 590
	AMSetAvatar = 591
	AMAuthenticateUser = 592
	AMAuthenticateUserResponse = 593
	AMGetAccountFriendsCount = 594
	AMGetAccountFriendsCountResponse = 595
	AMP2PIntroducerMessage = 596
	ClientChatAction = 597
	AMClientChatActionRelay = 598
	BaseVS = 600
	ReqChallenge = 600
	VACResponse = 601
	ReqChallengeTest = 602
	VSMarkCheat = 604
	VSAddCheat = 605
	VSPurgeCodeModDB = 606
	VSGetChallengeResults = 607
	VSChallengeResultText = 608
	VSReportLingerer = 609
	VSRequestManagedChallenge = 610
	VSLoadDBFinished = 611
	BaseDRMS = 625
	DRMBuildBlobRequest = 628
	DRMBuildBlobResponse = 629
	DRMResolveGuidRequest = 630
	DRMResolveGuidResponse = 631
	DRMVariabilityReport = 633
	DRMVariabilityReportResponse = 634
	DRMStabilityReport = 635
	DRMStabilityReportResponse = 636
	DRMDetailsReportRequest = 637
	DRMDetailsReportResponse = 638
	DRMProcessFile = 639
	DRMAdminUpdate = 640
	DRMAdminUpdateResponse = 641
	DRMSync = 642
	DRMSyncResponse = 643
	DRMProcessFileResponse = 644
	DRMEmptyGuidCache = 645
	DRMEmptyGuidCacheResponse = 646
	BaseCS = 650
	CSUserContentRequest = 652
	BaseClient = 700
	ClientLogOn_Deprecated = 701
	ClientAnonLogOn_Deprecated = 702
	ClientHeartBeat = 703
	ClientVACResponse = 704

	ClientGamesPlayed_obsolete = 705
	ClientLogOff = 706
	ClientNoUDPConnectivity = 707
	ClientInformOfCreateAccount = 708
	ClientAckVACBan = 709
	ClientConnectionStats = 710
	ClientInitPurchase = 711
	ClientPingResponse = 712
	ClientRemoveFriend = 714
	ClientGamesPlayedNoDataBlob = 715
	ClientChangeStatus = 716
	ClientVacStatusResponse = 717
	ClientFriendMsg = 718

	ClientGameConnect_obsolete = 719

	ClientGamesPlayed2_obsolete = 720

	ClientGameEnded_obsolete = 721
	ClientGetFinalPrice = 722
	ClientSystemIM = 726
	ClientSystemIMAck = 727
	ClientGetLicenses = 728
	ClientCancelLicense = 729
	ClientGetLegacyGameKey = 730

	ClientContentServerLogOn_Deprecated = 731
	ClientAckVACBan2 = 732
	ClientAckMessageByGID = 735
	ClientGetPurchaseReceipts = 736
	ClientAckPurchaseReceipt = 737
	ClientGamesPlayed3_obsolete = 738
	ClientSendGuestPass = 739
	ClientAckGuestPass = 740
	ClientRedeemGuestPass = 741
	ClientGamesPlayed = 742
	ClientRegisterKey = 743
	ClientInviteUserToClan = 744
	ClientAcknowledgeClanInvite = 745
	ClientPurchaseWithMachineID = 746
	ClientAppUsageEvent = 747
	ClientGetGiftTargetList = 748
	ClientGetGiftTargetListResponse = 749
	ClientLogOnResponse = 751
	ClientVACChallenge = 753
	ClientSetHeartbeatRate = 755
	ClientNotLoggedOnDeprecated = 756
	ClientLoggedOff = 757
	GSApprove = 758
	GSDeny = 759
	GSKick = 760
	ClientCreateAcctResponse = 761
	ClientPurchaseResponse = 763
	ClientPing = 764
	ClientNOP = 765
	ClientPersonaState = 766
	ClientFriendsList = 767
	ClientAccountInfo = 768
	ClientVacStatusQuery = 770
	ClientNewsUpdate = 771
	ClientGameConnectDeny = 773
	GSStatusReply = 774
	ClientGetFinalPriceResponse = 775
	ClientGameConnectTokens = 779
	ClientLicenseList = 780
	ClientCancelLicenseResponse = 781
	ClientVACBanStatus = 782
	ClientCMList = 783
	ClientEncryptPct = 784
	ClientGetLegacyGameKeyResponse = 785
	ClientFavoritesList = 786
	CSUserContentApprove = 787
	CSUserContentDeny = 788
	ClientInitPurchaseResponse = 789
	ClientAddFriend = 791
	ClientAddFriendResponse = 792
	ClientInviteFriend = 793
	ClientInviteFriendResponse = 794
	ClientSendGuestPassResponse = 795
	ClientAckGuestPassResponse = 796
	ClientRedeemGuestPassResponse = 797
	ClientUpdateGuestPassesList = 798
	ClientChatMsg = 799
	ClientChatInvite = 800
	ClientJoinChat = 801
	ClientChatMemberInfo = 802

	ClientLogOnWithCredentials_Deprecated = 803
	ClientPasswordChangeResponse = 805
	ClientChatEnter = 807
	ClientFriendRemovedFromSource = 808
	ClientCreateChat = 809
	ClientCreateChatResponse = 810
	ClientUpdateChatMetadata = 811
	ClientP2PIntroducerMessage = 813
	ClientChatActionResult = 814
	ClientRequestFriendData = 815
	ClientGetUserStats = 818
	ClientGetUserStatsResponse = 819
	ClientStoreUserStats = 820
	ClientStoreUserStatsResponse = 821
	ClientClanState = 822
	ClientServiceModule = 830
	ClientServiceCall = 831
	ClientServiceCallResponse = 832
	ClientPackageInfoRequest = 833
	ClientPackageInfoResponse = 834
	ClientNatTraversalStatEvent = 839
	ClientAppInfoRequest = 840
	ClientAppInfoResponse = 841
	ClientSteamUsageEvent = 842
	ClientCheckPassword = 845
	ClientResetPassword = 846
	ClientCheckPasswordResponse = 848
	ClientResetPasswordResponse = 849
	ClientSessionToken = 850
	ClientDRMProblemReport = 851
	ClientSetIgnoreFriend = 855
	ClientSetIgnoreFriendResponse = 856
	ClientGetAppOwnershipTicket = 857
	ClientGetAppOwnershipTicketResponse = 858
	ClientGetLobbyListResponse = 860
	ClientGetLobbyMetadata = 861
	ClientGetLobbyMetadataResponse = 862
	ClientVTTCert = 863
	ClientAppInfoUpdate = 866
	ClientAppInfoChanges = 867
	ClientServerList = 880
	ClientEmailChangeResponse = 891
	ClientSecretQAChangeResponse = 892
	ClientDRMBlobRequest = 896
	ClientDRMBlobResponse = 897
	ClientLookupKey = 898
	ClientLookupKeyResponse = 899
	
	ChannelEncryptRequest = 1303
	ChannelEncryptResponse = 1304
	ChannelEncryptResult = 1305

	ClientFriendMsgIncoming = 5427
	ClientLogon = 5514

	PICSBase = 8900
	PICSChangesSinceRequest = 8901
	PICSChangesSinceResponse = 8902
	PICSProductInfoRequest = 8903
	PICSProductInfoResponse = 8904
	PICSAccessTokenRequest = 8905
	PICSAccessTokenResponse = 8906
	
	ClientGetDepotDecryptionKey = 5438
	ClientGetDepotDecryptionKeyResponse = 5439
		
	ClientUpdateMachineAuth = 5537
	ClientUpdateMachineAuthResponse = 5538
		
class EUniverse:
	Invalid = 0
	Public = 1

class EAccountType:
	Invalid = 0
	Individual = 1
	Multiseat = 2
	GameServer = 3
	AnonGameServer = 4
	Pending = 5
	ContentServer = 6
	Clan = 7
	Chat = 8
	ConsoleUser = 9
	AnonUser = 10
	Max = 11
	
class EResult:
	Invalid = 0
	OK = 1
	Fail = 2
	NoConnection = 3
	InvalidPassword = 5
	LoggedInElsewhere = 6
	InvalidProtocolVer = 7
	InvalidParam = 8
	FileNotFound = 9
	Busy = 10
	InvalidState = 11
	InvalidName = 12
	InvalidEmail = 13
	DuplicateName = 14
	AccessDenied = 15
	Timeout = 16
	Banned = 17
	AccountNotFound = 18
	InvalidSteamID = 19
	ServiceUnavailable = 20
	NotLoggedOn = 21
	Pending = 22
	EncryptionFailure = 23
	InsufficientPrivilege = 24
	LimitExceeded = 25
	Revoked = 26
	Expired = 27
	AlreadyRedeemed = 28
	DuplicateRequest = 29
	AlreadyOwned = 30
	IPNotFound = 31
	PersistFailed = 32
	LockingFailed = 33
	LogonSessionReplaced = 34
	ConnectFailed = 35
	HandshakeFailed = 36
	IOFailure = 37
	RemoteDisconnect = 38
	ShoppingCartNotFound = 39
	Blocked = 40
	Ignored = 41
	NoMatch = 42
	AccountDisabled = 43
	ServiceReadOnly = 44
	AccountNotFeatured = 45
	AdministratorOK = 46
	ContentVersion = 47
	TryAnotherCM = 48
	PasswordRequiredToKickSession = 49
	AlreadyLoggedInElsewhere = 50
	Suspended = 51
	Cancelled = 52
	DataCorruption = 53
	DiskFull = 54
	RemoteCallFailed = 55
	PasswordNotSet = 56
	PSNAccountNotLinked = 57
	InvalidPSNTicket = 58
	PSNAccountAlreadyLinked = 59
	RemoteFileConflict = 60
	IllegalPassword = 61
	SameAsPreviousValue = 62
	AccountLogonDenied = 63
	CannotUseOldPassword = 64
	InvalidLoginAuthCode = 65
	AccountLogonDeniedNoMailSent = 66
	HardwareNotCapableOfIPT = 67
	IPTInitError = 68
	ParentalControlRestricted = 69
	FacebookQueryError = 70
	ExpiredLoginAuthCode = 71
	IPLoginRestrictionFailed = 72
	AccountLocked = 73
	AccountLogonDeniedVerifiedEmailRequired = 74
	NoMatchingURL = 75
	BadResponse = 76
	RequirePasswordReEntry = 77

class EPersonaState:
    Offline = 0
    Online = 1
    Busy = 2
    Away = 3
    Snooze = 4
    LookingToTrade = 5
    LookingToPlay = 6
    Max = 7

class EChatEntryType:
    Invalid = 0
    ChatMsg = 1
    Typing = 2
    InviteGame = 3
    Emote = 4
    LobbyGameStart = 5
    LeftConversation = 6
    Max = 7
	
class EServerType:
	CM = 7
	CS = 36
	GC = 37
	
class EDepotFileFlag:
	UserConfig = 1
	VersionedUserConfig = 2
	Encrypted = 4
	ReadOnly = 8
	Hidden = 16
	Executable = 32
	Directory = 64
	CustomExecutable = 128
	
class UniverseKeys:
	Public = bytearray([
				0x30, 0x81, 0x9D, 0x30, 0x0D, 0x06, 0x09, 0x2A, 0x86, 0x48, 0x86, 0xF7, 0x0D, 0x01, 0x01, 0x01,
				0x05, 0x00, 0x03, 0x81, 0x8B, 0x00, 0x30, 0x81, 0x87, 0x02, 0x81, 0x81, 0x00, 0xDF, 0xEC, 0x1A, 
				0xD6, 0x2C, 0x10, 0x66, 0x2C, 0x17, 0x35, 0x3A, 0x14, 0xB0, 0x7C, 0x59, 0x11, 0x7F, 0x9D, 0xD3, 
				0xD8, 0x2B, 0x7A, 0xE3, 0xE0, 0x15, 0xCD, 0x19, 0x1E, 0x46, 0xE8, 0x7B, 0x87, 0x74, 0xA2, 0x18, 
				0x46, 0x31, 0xA9, 0x03, 0x14, 0x79, 0x82, 0x8E, 0xE9, 0x45, 0xA2, 0x49, 0x12, 0xA9, 0x23, 0x68, 
				0x73, 0x89, 0xCF, 0x69, 0xA1, 0xB1, 0x61, 0x46, 0xBD, 0xC1, 0xBE, 0xBF, 0xD6, 0x01, 0x1B, 0xD8, 
				0x81, 0xD4, 0xDC, 0x90, 0xFB, 0xFE, 0x4F, 0x52, 0x73, 0x66, 0xCB, 0x95, 0x70, 0xD7, 0xC5, 0x8E, 
				0xBA, 0x1C, 0x7A, 0x33, 0x75, 0xA1, 0x62, 0x34, 0x46, 0xBB, 0x60, 0xB7, 0x80, 0x68, 0xFA, 0x13, 
				0xA7, 0x7A, 0x8A, 0x37, 0x4B, 0x9E, 0xC6, 0xF4, 0x5D, 0x5F, 0x3A, 0x99, 0xF9, 0x9E, 0xC4, 0x3A, 
				0xE9, 0x63, 0xA2, 0xBB, 0x88, 0x19, 0x28, 0xE0, 0xE7, 0x14, 0xC0, 0x42, 0x89, 0x02, 0x01, 0x11 ])
