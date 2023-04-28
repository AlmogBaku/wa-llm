from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KeepType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNKNOWN: _ClassVar[KeepType]
    KEEP_FOR_ALL: _ClassVar[KeepType]
    UNDO_KEEP_FOR_ALL: _ClassVar[KeepType]

class PeerDataOperationRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UPLOAD_STICKER: _ClassVar[PeerDataOperationRequestType]
    SEND_RECENT_STICKER_BOOTSTRAP: _ClassVar[PeerDataOperationRequestType]
    GENERATE_LINK_PREVIEW: _ClassVar[PeerDataOperationRequestType]
    HISTORY_SYNC_ON_DEMAND: _ClassVar[PeerDataOperationRequestType]
    PLACEHOLDER_MESSAGE_RESEND: _ClassVar[PeerDataOperationRequestType]

class MediaVisibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DEFAULT: _ClassVar[MediaVisibility]
    OFF: _ClassVar[MediaVisibility]
    ON: _ClassVar[MediaVisibility]
UNKNOWN: KeepType
KEEP_FOR_ALL: KeepType
UNDO_KEEP_FOR_ALL: KeepType
UPLOAD_STICKER: PeerDataOperationRequestType
SEND_RECENT_STICKER_BOOTSTRAP: PeerDataOperationRequestType
GENERATE_LINK_PREVIEW: PeerDataOperationRequestType
HISTORY_SYNC_ON_DEMAND: PeerDataOperationRequestType
PLACEHOLDER_MESSAGE_RESEND: PeerDataOperationRequestType
DEFAULT: MediaVisibility
OFF: MediaVisibility
ON: MediaVisibility

class ADVSignedKeyIndexList(_message.Message):
    __slots__ = ["details", "accountSignature"]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTSIGNATURE_FIELD_NUMBER: _ClassVar[int]
    details: bytes
    accountSignature: bytes
    def __init__(self, details: _Optional[bytes] = ..., accountSignature: _Optional[bytes] = ...) -> None: ...

class ADVSignedDeviceIdentity(_message.Message):
    __slots__ = ["details", "accountSignatureKey", "accountSignature", "deviceSignature"]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTSIGNATUREKEY_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTSIGNATURE_FIELD_NUMBER: _ClassVar[int]
    DEVICESIGNATURE_FIELD_NUMBER: _ClassVar[int]
    details: bytes
    accountSignatureKey: bytes
    accountSignature: bytes
    deviceSignature: bytes
    def __init__(self, details: _Optional[bytes] = ..., accountSignatureKey: _Optional[bytes] = ..., accountSignature: _Optional[bytes] = ..., deviceSignature: _Optional[bytes] = ...) -> None: ...

class ADVSignedDeviceIdentityHMAC(_message.Message):
    __slots__ = ["details", "hmac"]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    HMAC_FIELD_NUMBER: _ClassVar[int]
    details: bytes
    hmac: bytes
    def __init__(self, details: _Optional[bytes] = ..., hmac: _Optional[bytes] = ...) -> None: ...

class ADVKeyIndexList(_message.Message):
    __slots__ = ["rawId", "timestamp", "currentIndex", "validIndexes"]
    RAWID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CURRENTINDEX_FIELD_NUMBER: _ClassVar[int]
    VALIDINDEXES_FIELD_NUMBER: _ClassVar[int]
    rawId: int
    timestamp: int
    currentIndex: int
    validIndexes: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, rawId: _Optional[int] = ..., timestamp: _Optional[int] = ..., currentIndex: _Optional[int] = ..., validIndexes: _Optional[_Iterable[int]] = ...) -> None: ...

class ADVDeviceIdentity(_message.Message):
    __slots__ = ["rawId", "timestamp", "keyIndex"]
    RAWID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    KEYINDEX_FIELD_NUMBER: _ClassVar[int]
    rawId: int
    timestamp: int
    keyIndex: int
    def __init__(self, rawId: _Optional[int] = ..., timestamp: _Optional[int] = ..., keyIndex: _Optional[int] = ...) -> None: ...

class DeviceProps(_message.Message):
    __slots__ = ["os", "version", "platformType", "requireFullSync", "historySyncConfig"]
    class PlatformType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[DeviceProps.PlatformType]
        CHROME: _ClassVar[DeviceProps.PlatformType]
        FIREFOX: _ClassVar[DeviceProps.PlatformType]
        IE: _ClassVar[DeviceProps.PlatformType]
        OPERA: _ClassVar[DeviceProps.PlatformType]
        SAFARI: _ClassVar[DeviceProps.PlatformType]
        EDGE: _ClassVar[DeviceProps.PlatformType]
        DESKTOP: _ClassVar[DeviceProps.PlatformType]
        IPAD: _ClassVar[DeviceProps.PlatformType]
        ANDROID_TABLET: _ClassVar[DeviceProps.PlatformType]
        OHANA: _ClassVar[DeviceProps.PlatformType]
        ALOHA: _ClassVar[DeviceProps.PlatformType]
        CATALINA: _ClassVar[DeviceProps.PlatformType]
        TCL_TV: _ClassVar[DeviceProps.PlatformType]
        IOS_PHONE: _ClassVar[DeviceProps.PlatformType]
        IOS_CATALYST: _ClassVar[DeviceProps.PlatformType]
        ANDROID_PHONE: _ClassVar[DeviceProps.PlatformType]
        ANDROID_AMBIGUOUS: _ClassVar[DeviceProps.PlatformType]
    UNKNOWN: DeviceProps.PlatformType
    CHROME: DeviceProps.PlatformType
    FIREFOX: DeviceProps.PlatformType
    IE: DeviceProps.PlatformType
    OPERA: DeviceProps.PlatformType
    SAFARI: DeviceProps.PlatformType
    EDGE: DeviceProps.PlatformType
    DESKTOP: DeviceProps.PlatformType
    IPAD: DeviceProps.PlatformType
    ANDROID_TABLET: DeviceProps.PlatformType
    OHANA: DeviceProps.PlatformType
    ALOHA: DeviceProps.PlatformType
    CATALINA: DeviceProps.PlatformType
    TCL_TV: DeviceProps.PlatformType
    IOS_PHONE: DeviceProps.PlatformType
    IOS_CATALYST: DeviceProps.PlatformType
    ANDROID_PHONE: DeviceProps.PlatformType
    ANDROID_AMBIGUOUS: DeviceProps.PlatformType
    class HistorySyncConfig(_message.Message):
        __slots__ = ["fullSyncDaysLimit", "fullSyncSizeMbLimit", "storageQuotaMb", "inlineInitialPayloadInE2EeMsg", "recentSyncDaysLimit"]
        FULLSYNCDAYSLIMIT_FIELD_NUMBER: _ClassVar[int]
        FULLSYNCSIZEMBLIMIT_FIELD_NUMBER: _ClassVar[int]
        STORAGEQUOTAMB_FIELD_NUMBER: _ClassVar[int]
        INLINEINITIALPAYLOADINE2EEMSG_FIELD_NUMBER: _ClassVar[int]
        RECENTSYNCDAYSLIMIT_FIELD_NUMBER: _ClassVar[int]
        fullSyncDaysLimit: int
        fullSyncSizeMbLimit: int
        storageQuotaMb: int
        inlineInitialPayloadInE2EeMsg: bool
        recentSyncDaysLimit: int
        def __init__(self, fullSyncDaysLimit: _Optional[int] = ..., fullSyncSizeMbLimit: _Optional[int] = ..., storageQuotaMb: _Optional[int] = ..., inlineInitialPayloadInE2EeMsg: bool = ..., recentSyncDaysLimit: _Optional[int] = ...) -> None: ...
    class AppVersion(_message.Message):
        __slots__ = ["primary", "secondary", "tertiary", "quaternary", "quinary"]
        PRIMARY_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_FIELD_NUMBER: _ClassVar[int]
        TERTIARY_FIELD_NUMBER: _ClassVar[int]
        QUATERNARY_FIELD_NUMBER: _ClassVar[int]
        QUINARY_FIELD_NUMBER: _ClassVar[int]
        primary: int
        secondary: int
        tertiary: int
        quaternary: int
        quinary: int
        def __init__(self, primary: _Optional[int] = ..., secondary: _Optional[int] = ..., tertiary: _Optional[int] = ..., quaternary: _Optional[int] = ..., quinary: _Optional[int] = ...) -> None: ...
    OS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PLATFORMTYPE_FIELD_NUMBER: _ClassVar[int]
    REQUIREFULLSYNC_FIELD_NUMBER: _ClassVar[int]
    HISTORYSYNCCONFIG_FIELD_NUMBER: _ClassVar[int]
    os: str
    version: DeviceProps.AppVersion
    platformType: DeviceProps.PlatformType
    requireFullSync: bool
    historySyncConfig: DeviceProps.HistorySyncConfig
    def __init__(self, os: _Optional[str] = ..., version: _Optional[_Union[DeviceProps.AppVersion, _Mapping]] = ..., platformType: _Optional[_Union[DeviceProps.PlatformType, str]] = ..., requireFullSync: bool = ..., historySyncConfig: _Optional[_Union[DeviceProps.HistorySyncConfig, _Mapping]] = ...) -> None: ...

class PaymentInviteMessage(_message.Message):
    __slots__ = ["serviceType", "expiryTimestamp"]
    class ServiceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[PaymentInviteMessage.ServiceType]
        FBPAY: _ClassVar[PaymentInviteMessage.ServiceType]
        NOVI: _ClassVar[PaymentInviteMessage.ServiceType]
        UPI: _ClassVar[PaymentInviteMessage.ServiceType]
    UNKNOWN: PaymentInviteMessage.ServiceType
    FBPAY: PaymentInviteMessage.ServiceType
    NOVI: PaymentInviteMessage.ServiceType
    UPI: PaymentInviteMessage.ServiceType
    SERVICETYPE_FIELD_NUMBER: _ClassVar[int]
    EXPIRYTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    serviceType: PaymentInviteMessage.ServiceType
    expiryTimestamp: int
    def __init__(self, serviceType: _Optional[_Union[PaymentInviteMessage.ServiceType, str]] = ..., expiryTimestamp: _Optional[int] = ...) -> None: ...

class OrderMessage(_message.Message):
    __slots__ = ["orderId", "thumbnail", "itemCount", "status", "surface", "message", "orderTitle", "sellerJid", "token", "totalAmount1000", "totalCurrencyCode", "contextInfo"]
    class OrderSurface(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        CATALOG: _ClassVar[OrderMessage.OrderSurface]
    CATALOG: OrderMessage.OrderSurface
    class OrderStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        INQUIRY: _ClassVar[OrderMessage.OrderStatus]
    INQUIRY: OrderMessage.OrderStatus
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    ITEMCOUNT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SURFACE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ORDERTITLE_FIELD_NUMBER: _ClassVar[int]
    SELLERJID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTALAMOUNT1000_FIELD_NUMBER: _ClassVar[int]
    TOTALCURRENCYCODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    orderId: str
    thumbnail: bytes
    itemCount: int
    status: OrderMessage.OrderStatus
    surface: OrderMessage.OrderSurface
    message: str
    orderTitle: str
    sellerJid: str
    token: str
    totalAmount1000: int
    totalCurrencyCode: str
    contextInfo: ContextInfo
    def __init__(self, orderId: _Optional[str] = ..., thumbnail: _Optional[bytes] = ..., itemCount: _Optional[int] = ..., status: _Optional[_Union[OrderMessage.OrderStatus, str]] = ..., surface: _Optional[_Union[OrderMessage.OrderSurface, str]] = ..., message: _Optional[str] = ..., orderTitle: _Optional[str] = ..., sellerJid: _Optional[str] = ..., token: _Optional[str] = ..., totalAmount1000: _Optional[int] = ..., totalCurrencyCode: _Optional[str] = ..., contextInfo: _Optional[_Union[ContextInfo, _Mapping]] = ...) -> None: ...

class LocationMessage(_message.Message):
    __slots__ = ["degreesLatitude", "degreesLongitude", "name", "address", "url", "isLive", "accuracyInMeters", "speedInMps", "degreesClockwiseFromMagneticNorth", "comment", "jpegThumbnail", "contextInfo"]
    DEGREESLATITUDE_FIELD_NUMBER: _ClassVar[int]
    DEGREESLONGITUDE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    ISLIVE_FIELD_NUMBER: _ClassVar[int]
    ACCURACYINMETERS_FIELD_NUMBER: _ClassVar[int]
    SPEEDINMPS_FIELD_NUMBER: _ClassVar[int]
    DEGREESCLOCKWISEFROMMAGNETICNORTH_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    JPEGTHUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    CONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    degreesLatitude: float
    degreesLongitude: float
    name: str
    address: str
    url: str
    isLive: bool
    accuracyInMeters: int
    speedInMps: float
    degreesClockwiseFromMagneticNorth: int
    comment: str
    jpegThumbnail: bytes
    contextInfo: ContextInfo
    def __init__(self, degreesLatitude: _Optional[float] = ..., degreesLongitude: _Optional[float] = ..., name: _Optional[str] = ..., address: _Optional[str] = ..., url: _Optional[str] = ..., isLive: bool = ..., accuracyInMeters: _Optional[int] = ..., speedInMps: _Optional[float] = ..., degreesClockwiseFromMagneticNorth: _Optional[int] = ..., comment: _Optional[str] = ..., jpegThumbnail: _Optional[bytes] = ..., contextInfo: _Optional[_Union[ContextInfo, _Mapping]] = ...) -> None: ...

class LiveLocationMessage(_message.Message):
    __slots__ = ["degreesLatitude", "degreesLongitude", "accuracyInMeters", "speedInMps", "degreesClockwiseFromMagneticNorth", "caption", "sequenceNumber", "timeOffset", "jpegThumbnail", "contextInfo"]
    DEGREESLATITUDE_FIELD_NUMBER: _ClassVar[int]
    DEGREESLONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ACCURACYINMETERS_FIELD_NUMBER: _ClassVar[int]
    SPEEDINMPS_FIELD_NUMBER: _ClassVar[int]
    DEGREESCLOCKWISEFROMMAGNETICNORTH_FIELD_NUMBER: _ClassVar[int]
    CAPTION_FIELD_NUMBER: _ClassVar[int]
    SEQUENCENUMBER_FIELD_NUMBER: _ClassVar[int]
    TIMEOFFSET_FIELD_NUMBER: _ClassVar[int]
    JPEGTHUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    CONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    degreesLatitude: float
    degreesLongitude: float
    accuracyInMeters: int
    speedInMps: float
    degreesClockwiseFromMagneticNorth: int
    caption: str
    sequenceNumber: int
    timeOffset: int
    jpegThumbnail: bytes
    contextInfo: ContextInfo
    def __init__(self, degreesLatitude: _Optional[float] = ..., degreesLongitude: _Optional[float] = ..., accuracyInMeters: _Optional[int] = ..., speedInMps: _Optional[float] = ..., degreesClockwiseFromMagneticNorth: _Optional[int] = ..., caption: _Optional[str] = ..., sequenceNumber: _Optional[int] = ..., timeOffset: _Optional[int] = ..., jpegThumbnail: _Optional[bytes] = ..., contextInfo: _Optional[_Union[ContextInfo, _Mapping]] = ...) -> None: ...

class ListResponseMessage(_message.Message):
    __slots__ = ["title", "listType", "singleSelectReply", "contextInfo", "description"]
    class ListType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[ListResponseMessage.ListType]
        SINGLE_SELECT: _ClassVar[ListResponseMessage.ListType]
    UNKNOWN: ListResponseMessage.ListType
    SINGLE_SELECT: ListResponseMessage.ListType
    class SingleSelectReply(_message.Message):
        __slots__ = ["selectedRowId"]
        SELECTEDROWID_FIELD_NUMBER: _ClassVar[int]
        selectedRowId: str
        def __init__(self, selectedRowId: _Optional[str] = ...) -> None: ...
    TITLE_FIELD_NUMBER: _ClassVar[int]
    LISTTYPE_FIELD_NUMBER: _ClassVar[int]
    SINGLESELECTREPLY_FIELD_NUMBER: _ClassVar[int]
    CONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    title: str
    listType: ListResponseMessage.ListType
    singleSelectReply: ListResponseMessage.SingleSelectReply
    contextInfo: ContextInfo
    description: str
    def __init__(self, title: _Optional[str] = ..., listType: _Optional[_Union[ListResponseMessage.ListType, str]] = ..., singleSelectReply: _Optional[_Union[ListResponseMessage.SingleSelectReply, _Mapping]] = ..., contextInfo: _Optional[_Union[ContextInfo, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...

class ListMessage(_message.Message):
    __slots__ = ["title", "description", "buttonText", "listType", "sections", "productListInfo", "footerText", "contextInfo"]
    class ListType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[ListMessage.ListType]
        SINGLE_SELECT: _ClassVar[ListMessage.ListType]
        PRODUCT_LIST: _ClassVar[ListMessage.ListType]
    UNKNOWN: ListMessage.ListType
    SINGLE_SELECT: ListMessage.ListType
    PRODUCT_LIST: ListMessage.ListType
    class Section(_message.Message):
        __slots__ = ["title", "rows"]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        ROWS_FIELD_NUMBER: _ClassVar[int]
        title: str
        rows: _containers.RepeatedCompositeFieldContainer[ListMessage.Row]
        def __init__(self, title: _Optional[str] = ..., rows: _Optional[_Iterable[_Union[ListMessage.Row, _Mapping]]] = ...) -> None: ...
    class Row(_message.Message):
        __slots__ = ["title", "description", "rowId"]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ROWID_FIELD_NUMBER: _ClassVar[int]
        title: str
        description: str
        rowId: str
        def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., rowId: _Optional[str] = ...) -> None: ...
    class Product(_message.Message):
        __slots__ = ["productId"]
        PRODUCTID_FIELD_NUMBER: _ClassVar[int]
        productId: str
        def __init__(self, productId: _Optional[str] = ...) -> None: ...
    class ProductSection(_message.Message):
        __slots__ = ["title", "products"]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        PRODUCTS_FIELD_NUMBER: _ClassVar[int]
        title: str
        products: _containers.RepeatedCompositeFieldContainer[ListMessage.Product]
        def __init__(self, title: _Optional[str] = ..., products: _Optional[_Iterable[_Union[ListMessage.Product, _Mapping]]] = ...) -> None: ...
    class ProductListInfo(_message.Message):
        __slots__ = ["productSections", "headerImage", "businessOwnerJid"]
        PRODUCTSECTIONS_FIELD_NUMBER: _ClassVar[int]
        HEADERIMAGE_FIELD_NUMBER: _ClassVar[int]
        BUSINESSOWNERJID_FIELD_NUMBER: _ClassVar[int]
        productSections: _containers.RepeatedCompositeFieldContainer[ListMessage.ProductSection]
        headerImage: ListMessage.ProductListHeaderImage
        businessOwnerJid: str
        def __init__(self, productSections: _Optional[_Iterable[_Union[ListMessage.ProductSection, _Mapping]]] = ..., headerImage: _Optional[_Union[ListMessage.ProductListHeaderImage, _Mapping]] = ..., businessOwnerJid: _Optional[str] = ...) -> None: ...
    class ProductListHeaderImage(_message.Message):
        __slots__ = ["productId", "jpegThumbnail"]
        PRODUCTID_FIELD_NUMBER: _ClassVar[int]
        JPEGTHUMBNAIL_FIELD_NUMBER: _ClassVar[int]
        productId: str
        jpegThumbnail: bytes
        def __init__(self, productId: _Optional[str] = ..., jpegThumbnail: _Optional[bytes] = ...) -> None: ...
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BUTTONTEXT_FIELD_NUMBER: _ClassVar[int]
    LISTTYPE_FIELD_NUMBER: _ClassVar[int]
    SECTIONS_FIELD_NUMBER: _ClassVar[int]
    PRODUCTLISTINFO_FIELD_NUMBER: _ClassVar[int]
    FOOTERTEXT_FIELD_NUMBER: _ClassVar[int]
    CONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    buttonText: str
    listType: ListMessage.ListType
    sections: _containers.RepeatedCompositeFieldContainer[ListMessage.Section]
    productListInfo: ListMessage.ProductListInfo
    footerText: str
    contextInfo: ContextInfo
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., buttonText: _Optional[str] = ..., listType: _Optional[_Union[ListMessage.ListType, str]] = ..., sections: _Optional[_Iterable[_Union[ListMessage.Section, _Mapping]]] = ..., productListInfo: _Optional[_Union[ListMessage.ProductListInfo, _Mapping]] = ..., footerText: _Optional[str] = ..., contextInfo: _Optional[_Union[ContextInfo, _Mapping]] = ...) -> None: ...

class KeepInChatMessage(_message.Message):
    __slots__ = ["key", "keepType", "timestampMs"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    KEEPTYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPMS_FIELD_NUMBER: _ClassVar[int]
    key: MessageKey
    keepType: KeepType
    timestampMs: int
    def __init__(self, key: _Optional[_Union[MessageKey, _Mapping]] = ..., keepType: _Optional[_Union[KeepType, str]] = ..., timestampMs: _Optional[int] = ...) -> None: ...

class InvoiceMessage(_message.Message):
    __slots__ = ["note", "token", "attachmentType", "attachmentMimetype", "attachmentMediaKey", "attachmentMediaKeyTimestamp", "attachmentFileSha256", "attachmentFileEncSha256", "attachmentDirectPath", "attachmentJpegThumbnail"]
    class AttachmentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        IMAGE: _ClassVar[InvoiceMessage.AttachmentType]
        PDF: _ClassVar[InvoiceMessage.AttachmentType]
    IMAGE: InvoiceMessage.AttachmentType
    PDF: InvoiceMessage.AttachmentType
    NOTE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTTYPE_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTMIMETYPE_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTMEDIAKEY_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTMEDIAKEYTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTFILESHA256_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTFILEENCSHA256_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTDIRECTPATH_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTJPEGTHUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    note: str
    token: str
    attachmentType: InvoiceMessage.AttachmentType
    attachmentMimetype: str
    attachmentMediaKey: bytes
    attachmentMediaKeyTimestamp: int
    attachmentFileSha256: bytes
    attachmentFileEncSha256: bytes
    attachmentDirectPath: str
    attachmentJpegThumbnail: bytes
    def __init__(self, note: _Optional[str] = ..., token: _Optional[str] = ..., attachmentType: _Optional[_Union[InvoiceMessage.AttachmentType, str]] = ..., attachmentMimetype: _Optional[str] = ..., attachmentMediaKey: _Optional[bytes] = ..., attachmentMediaKeyTimestamp: _Optional[int] = ..., attachmentFileSha256: _Optional[bytes] = ..., attachmentFileEncSha256: _Optional[bytes] = ..., attachmentDirectPath: _Optional[str] = ..., attachmentJpegThumbnail: _Optional[bytes] = ...) -> None: ...

class InteractiveResponseMessage(_message.Message):
    __slots__ = ["body", "contextInfo", "nativeFlowResponseMessage"]
    class NativeFlowResponseMessage(_message.Message):
        __slots__ = ["name", "paramsJson", "version"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PARAMSJSON_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        name: str
        paramsJson: str
        version: int
        def __init__(self, name: _Optional[str] = ..., paramsJson: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...
    class Body(_message.Message):
        __slots__ = ["text", "format"]
        class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            DEFAULT: _ClassVar[InteractiveResponseMessage.Body.Format]
            EXTENSIONS_1: _ClassVar[InteractiveResponseMessage.Body.Format]
        DEFAULT: InteractiveResponseMessage.Body.Format
        EXTENSIONS_1: InteractiveResponseMessage.Body.Format
        TEXT_FIELD_NUMBER: _ClassVar[int]
        FORMAT_FIELD_NUMBER: _ClassVar[int]
        text: str
        format: InteractiveResponseMessage.Body.Format
        def __init__(self, text: _Optional[str] = ..., format: _Optional[_Union[InteractiveResponseMessage.Body.Format, str]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    CONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    NATIVEFLOWRESPONSEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    body: InteractiveResponseMessage.Body
    contextInfo: ContextInfo
    nativeFlowResponseMessage: InteractiveResponseMessage.NativeFlowResponseMessage
    def __init__(self, body: _Optional[_Union[InteractiveResponseMessage.Body, _Mapping]] = ..., contextInfo: _Optional[_Union[ContextInfo, _Mapping]] = ..., nativeFlowResponseMessage: _Optional[_Union[InteractiveResponseMessage.NativeFlowResponseMessage, _Mapping]] = ...) -> None: ...

class InteractiveMessage(_message.Message):
    __slots__ = ["header", "body", "footer", "contextInfo", "shopStorefrontMessage", "collectionMessage", "nativeFlowMessage"]
    class ShopMessage(_message.Message):
        __slots__ = ["id", "surface", "messageVersion"]
        class Surface(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            UNKNOWN_SURFACE: _ClassVar[InteractiveMessage.ShopMessage.Surface]
            FB: _ClassVar[InteractiveMessage.ShopMessage.Surface]
            IG: _ClassVar[InteractiveMessage.ShopMessage.Surface]
            WA: _ClassVar[InteractiveMessage.ShopMessage.Surface]
        UNKNOWN_SURFACE: InteractiveMessage.ShopMessage.Surface
        FB: InteractiveMessage.ShopMessage.Surface
        IG: InteractiveMessage.ShopMessage.Surface
        WA: InteractiveMessage.ShopMessage.Surface
        ID_FIELD_NUMBER: _ClassVar[int]
        SURFACE_FIELD_NUMBER: _ClassVar[int]
        MESSAGEVERSION_FIELD_NUMBER: _ClassVar[int]
        id: str
        surface: InteractiveMessage.ShopMessage.Surface
        messageVersion: int
        def __init__(self, id: _Optional[str] = ..., surface: _Optional[_Union[InteractiveMessage.ShopMessage.Surface, str]] = ..., messageVersion: _Optional[int] = ...) -> None: ...
    class NativeFlowMessage(_message.Message):
        __slots__ = ["buttons", "messageParamsJson", "messageVersion"]
        class NativeFlowButton(_message.Message):
            __slots__ = ["name", "buttonParamsJson"]
            NAME_FIELD_NUMBER: _ClassVar[int]
            BUTTONPARAMSJSON_FIELD_NUMBER: _ClassVar[int]
            name: str
            buttonParamsJson: str
            def __init__(self, name: _Optional[str] = ..., buttonParamsJson: _Optional[str] = ...) -> None: ...
        BUTTONS_FIELD_NUMBER: _ClassVar[int]
        MESSAGEPARAMSJSON_FIELD_NUMBER: _ClassVar[int]
        MESSAGEVERSION_FIELD_NUMBER: _ClassVar[int]
        buttons: _containers.RepeatedCompositeFieldContainer[InteractiveMessage.NativeFlowMessage.NativeFlowButton]
        messageParamsJson: str
        messageVersion: int
        def __init__(self, buttons: _Optional[_Iterable[_Union[InteractiveMessage.NativeFlowMessage.NativeFlowButton, _Mapping]]] = ..., messageParamsJson: _Optional[str] = ..., messageVersion: _Optional[int] = ...) -> None: ...
    class Header(_message.Message):
        __slots__ = ["title", "subtitle", "hasMediaAttachment", "documentMessage", "imageMessage", "jpegThumbnail", "videoMessage"]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        HASMEDIAATTACHMENT_FIELD_NUMBER: _ClassVar[int]
        DOCUMENTMESSAGE_FIELD_NUMBER: _ClassVar[int]
        IMAGEMESSAGE_FIELD_NUMBER: _ClassVar[int]
        JPEGTHUMBNAIL_FIELD_NUMBER: _ClassVar[int]
        VIDEOMESSAGE_FIELD_NUMBER: _ClassVar[int]
        title: str
        subtitle: str
        hasMediaAttachment: bool
        documentMessage: DocumentMessage
        imageMessage: ImageMessage
        jpegThumbnail: bytes
        videoMessage: VideoMessage
        def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., hasMediaAttachment: bool = ..., documentMessage: _Optional[_Union[DocumentMessage, _Mapping]] = ..., imageMessage: _Optional[_Union[ImageMessage, _Mapping]] = ..., jpegThumbnail: _Optional[bytes] = ..., videoMessage: _Optional[_Union[VideoMessage, _Mapping]] = ...) -> None: ...
    class Footer(_message.Message):
        __slots__ = ["text"]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        text: str
        def __init__(self, text: _Optional[str] = ...) -> None: ...
    class CollectionMessage(_message.Message):
        __slots__ = ["bizJid", "id", "messageVersion"]
        BIZJID_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        MESSAGEVERSION_FIELD_NUMBER: _ClassVar[int]
        bizJid: str
        id: str
        messageVersion: int
        def __init__(self, bizJid: _Optional[str] = ..., id: _Optional[str] = ..., messageVersion: _Optional[int] = ...) -> None: ...
    class Body(_message.Message):
        __slots__ = ["text"]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        text: str
        def __init__(self, text: _Optional[str] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    FOOTER_FIELD_NUMBER: _ClassVar[int]
    CONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    SHOPSTOREFRONTMESSAGE_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONMESSAGE_FIELD_NUMBER: _ClassVar[int]
    NATIVEFLOWMESSAGE_FIELD_NUMBER: _ClassVar[int]
    header: InteractiveMessage.Header
    body: InteractiveMessage.Body
    footer: InteractiveMessage.Footer
    contextInfo: ContextInfo
    shopStorefrontMessage: InteractiveMessage.ShopMessage
    collectionMessage: InteractiveMessage.CollectionMessage
    nativeFlowMessage: InteractiveMessage.NativeFlowMessage
    def __init__(self, header: _Optional[_Union[InteractiveMessage.Header, _Mapping]] = ..., body: _Optional[_Union[InteractiveMessage.Body, _Mapping]] = ..., footer: _Optional[_Union[InteractiveMessage.Footer, _Mapping]] = ..., contextInfo: _Optional[_Union[ContextInfo, _Mapping]] = ..., shopStorefrontMessage: _Optional[_Union[InteractiveMessage.ShopMessage, _Mapping]] = ..., collectionMessage: _Optional[_Union[InteractiveMessage.CollectionMessage, _Mapping]] = ..., nativeFlowMessage: _Optional[_Union[InteractiveMessage.NativeFlowMessage, _Mapping]] = ...) -> None: ...

class InitialSecurityNotificationSettingSync(_message.Message):
    __slots__ = ["securityNotificationEnabled"]
    SECURITYNOTIFICATIONENABLED_FIELD_NUMBER: _ClassVar[int]
    securityNotificationEnabled: bool
    def __init__(self, securityNotificationEnabled: bool = ...) -> None: ...

class ImageMessage(_message.Message):
    __slots__ = ["url", "mimetype", "caption", "fileSha256", "fileLength", "height", "width", "mediaKey", "fileEncSha256", "interactiveAnnotations", "directPath", "mediaKeyTimestamp", "jpegThumbnail", "contextInfo", "firstScanSidecar", "firstScanLength", "experimentGroupId", "scansSidecar", "scanLengths", "midQualityFileSha256", "midQualityFileEncSha256", "viewOnce", "thumbnailDirectPath", "thumbnailSha256", "thumbnailEncSha256", "staticUrl"]
    URL_FIELD_NUMBER: _ClassVar[int]
    MIMETYPE_FIELD_NUMBER: _ClassVar[int]
    CAPTION_FIELD_NUMBER: _ClassVar[int]
    FILESHA256_FIELD_NUMBER: _ClassVar[int]
    FILELENGTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    MEDIAKEY_FIELD_NUMBER: _ClassVar[int]
    FILEENCSHA256_FIELD_NUMBER: _ClassVar[int]
    INTERACTIVEANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    DIRECTPATH_FIELD_NUMBER: _ClassVar[int]
    MEDIAKEYTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    JPEGTHUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    CONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    FIRSTSCANSIDECAR_FIELD_NUMBER: _ClassVar[int]
    FIRSTSCANLENGTH_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENTGROUPID_FIELD_NUMBER: _ClassVar[int]
    SCANSSIDECAR_FIELD_NUMBER: _ClassVar[int]
    SCANLENGTHS_FIELD_NUMBER: _ClassVar[int]
    MIDQUALITYFILESHA256_FIELD_NUMBER: _ClassVar[int]
    MIDQUALITYFILEENCSHA256_FIELD_NUMBER: _ClassVar[int]
    VIEWONCE_FIELD_NUMBER: _ClassVar[int]
    THUMBNAILDIRECTPATH_FIELD_NUMBER: _ClassVar[int]
    THUMBNAILSHA256_FIELD_NUMBER: _ClassVar[int]
    THUMBNAILENCSHA256_FIELD_NUMBER: _ClassVar[int]
    STATICURL_FIELD_NUMBER: _ClassVar[int]
    url: str
    mimetype: str
    caption: str
    fileSha256: bytes
    fileLength: int
    height: int
    width: int
    mediaKey: bytes
    fileEncSha256: bytes
    interactiveAnnotations: _containers.RepeatedCompositeFieldContainer[InteractiveAnnotation]
    directPath: str
    mediaKeyTimestamp: int
    jpegThumbnail: bytes
    contextInfo: ContextInfo
    firstScanSidecar: bytes
    firstScanLength: int
    experimentGroupId: int
    scansSidecar: bytes
    scanLengths: _containers.RepeatedScalarFieldContainer[int]
    midQualityFileSha256: bytes
    midQualityFileEncSha256: bytes
    viewOnce: bool
    thumbnailDirectPath: str
    thumbnailSha256: bytes
    thumbnailEncSha256: bytes
    staticUrl: str
    def __init__(self, url: _Optional[str] = ..., mimetype: _Optional[str] = ..., caption: _Optional[str] = ..., fileSha256: _Optional[bytes] = ..., fileLength: _Optional[int] = ..., height: _Optional[int] = ..., width: _Optional[int] = ..., mediaKey: _Optional[bytes] = ..., fileEncSha256: _Optional[bytes] = ..., interactiveAnnotations: _Optional[_Iterable[_Union[InteractiveAnnotation, _Mapping]]] = ..., directPath: _Optional[str] = ..., mediaKeyTimestamp: _Optional[int] = ..., jpegThumbnail: _Optional[bytes] = ..., contextInfo: _Optional[_Union[ContextInfo, _Mapping]] = ..., firstScanSidecar: _Optional[bytes] = ..., firstScanLength: _Optional[int] = ..., experimentGroupId: _Optional[int] = ..., scansSidecar: _Optional[bytes] = ..., scanLengths: _Optional[_Iterable[int]] = ..., midQualityFileSha256: _Optional[bytes] = ..., midQualityFileEncSha256: _Optional[bytes] = ..., viewOnce: bool = ..., thumbnailDirectPath: _Optional[str] = ..., thumbnailSha256: _Optional[bytes] = ..., thumbnailEncSha256: _Optional[bytes] = ..., staticUrl: _Optional[str] = ...) -> None: ...

class HistorySyncNotification(_message.Message):
    __slots__ = ["fileSha256", "fileLength", "mediaKey", "fileEncSha256", "directPath", "syncType", "chunkOrder", "originalMessageId", "progress", "oldestMsgInChunkTimestampSec", "initialHistBootstrapInlinePayload"]
    class HistorySyncType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        INITIAL_BOOTSTRAP: _ClassVar[HistorySyncNotification.HistorySyncType]
        INITIAL_STATUS_V3: _ClassVar[HistorySyncNotification.HistorySyncType]
        FULL: _ClassVar[HistorySyncNotification.HistorySyncType]
        RECENT: _ClassVar[HistorySyncNotification.HistorySyncType]
        PUSH_NAME: _ClassVar[HistorySyncNotification.HistorySyncType]
        NON_BLOCKING_DATA: _ClassVar[HistorySyncNotification.HistorySyncType]
        ON_DEMAND: _ClassVar[HistorySyncNotification.HistorySyncType]
    INITIAL_BOOTSTRAP: HistorySyncNotification.HistorySyncType
    INITIAL_STATUS_V3: HistorySyncNotification.HistorySyncType
    FULL: HistorySyncNotification.HistorySyncType
    RECENT: HistorySyncNotification.HistorySyncType
    PUSH_NAME: HistorySyncNotification.HistorySyncType
    NON_BLOCKING_DATA: HistorySyncNotification.HistorySyncType
    ON_DEMAND: HistorySyncNotification.HistorySyncType
    FILESHA256_FIELD_NUMBER: _ClassVar[int]
    FILELENGTH_FIELD_NUMBER: _ClassVar[int]
    MEDIAKEY_FIELD_NUMBER: _ClassVar[int]
    FILEENCSHA256_FIELD_NUMBER: _ClassVar[int]
    DIRECTPATH_FIELD_NUMBER: _ClassVar[int]
    SYNCTYPE_FIELD_NUMBER: _ClassVar[int]
    CHUNKORDER_FIELD_NUMBER: _ClassVar[int]
    ORIGINALMESSAGEID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    OLDESTMSGINCHUNKTIMESTAMPSEC_FIELD_NUMBER: _ClassVar[int]
    INITIALHISTBOOTSTRAPINLINEPAYLOAD_FIELD_NUMBER: _ClassVar[int]
    fileSha256: bytes
    fileLength: int
    mediaKey: bytes
    fileEncSha256: bytes
    directPath: str
    syncType: HistorySyncNotification.HistorySyncType
    chunkOrder: int
    originalMessageId: str
    progress: int
    oldestMsgInChunkTimestampSec: int
    initialHistBootstrapInlinePayload: bytes
    def __init__(self, fileSha256: _Optional[bytes] = ..., fileLength: _Optional[int] = ..., mediaKey: _Optional[bytes] = ..., fileEncSha256: _Optional[bytes] = ..., directPath: _Optional[str] = ..., syncType: _Optional[_Union[HistorySyncNotification.HistorySyncType, str]] = ..., chunkOrder: _Optional[int] = ..., originalMessageId: _Optional[str] = ..., progress: _Optional[int] = ..., oldestMsgInChunkTimestampSec: _Optional[int] = ..., initialHistBootstrapInlinePayload: _Optional[bytes] = ...) -> None: ...

class HighlyStructuredMessage(_message.Message):
    __slots__ = ["namespace", "elementName", "params", "fallbackLg", "fallbackLc", "localizableParams", "deterministicLg", "deterministicLc", "hydratedHsm"]
    class HSMLocalizableParameter(_message.Message):
        __slots__ = ["default", "currency", "dateTime"]
        class HSMDateTime(_message.Message):
            __slots__ = ["component", "unixEpoch"]
            class HSMDateTimeUnixEpoch(_message.Message):
                __slots__ = ["timestamp"]
                TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
                timestamp: int
                def __init__(self, timestamp: _Optional[int] = ...) -> None: ...
            class HSMDateTimeComponent(_message.Message):
                __slots__ = ["dayOfWeek", "year", "month", "dayOfMonth", "hour", "minute", "calendar"]
                class DayOfWeekType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = []
                    MONDAY: _ClassVar[HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent.DayOfWeekType]
                    TUESDAY: _ClassVar[HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent.DayOfWeekType]
                    WEDNESDAY: _ClassVar[HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent.DayOfWeekType]
                    THURSDAY: _ClassVar[HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent.DayOfWeekType]
                    FRIDAY: _ClassVar[HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent.DayOfWeekType]
                    SATURDAY: _ClassVar[HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent.DayOfWeekType]
                    SUNDAY: _ClassVar[HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent.DayOfWeekType]
                MONDAY: HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent.DayOfWeekType
                TUESDAY: HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent.DayOfWeekType
                WEDNESDAY: HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent.DayOfWeekType
                THURSDAY: HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent.DayOfWeekType
                FRIDAY: HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent.DayOfWeekType
                SATURDAY: HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent.DayOfWeekType
                SUNDAY: HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent.DayOfWeekType
                class CalendarType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = []
                    GREGORIAN: _ClassVar[HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent.CalendarType]
                    SOLAR_HIJRI: _ClassVar[HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent.CalendarType]
                GREGORIAN: HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent.CalendarType
                SOLAR_HIJRI: HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent.CalendarType
                DAYOFWEEK_FIELD_NUMBER: _ClassVar[int]
                YEAR_FIELD_NUMBER: _ClassVar[int]
                MONTH_FIELD_NUMBER: _ClassVar[int]
                DAYOFMONTH_FIELD_NUMBER: _ClassVar[int]
                HOUR_FIELD_NUMBER: _ClassVar[int]
                MINUTE_FIELD_NUMBER: _ClassVar[int]
                CALENDAR_FIELD_NUMBER: _ClassVar[int]
                dayOfWeek: HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent.DayOfWeekType
                year: int
                month: int
                dayOfMonth: int
                hour: int
                minute: int
                calendar: HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent.CalendarType
                def __init__(self, dayOfWeek: _Optional[_Union[HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent.DayOfWeekType, str]] = ..., year: _Optional[int] = ..., month: _Optional[int] = ..., dayOfMonth: _Optional[int] = ..., hour: _Optional[int] = ..., minute: _Optional[int] = ..., calendar: _Optional[_Union[HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent.CalendarType, str]] = ...) -> None: ...
            COMPONENT_FIELD_NUMBER: _ClassVar[int]
            UNIXEPOCH_FIELD_NUMBER: _ClassVar[int]
            component: HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent
            unixEpoch: HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeUnixEpoch
            def __init__(self, component: _Optional[_Union[HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeComponent, _Mapping]] = ..., unixEpoch: _Optional[_Union[HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime.HSMDateTimeUnixEpoch, _Mapping]] = ...) -> None: ...
        class HSMCurrency(_message.Message):
            __slots__ = ["currencyCode", "amount1000"]
            CURRENCYCODE_FIELD_NUMBER: _ClassVar[int]
            AMOUNT1000_FIELD_NUMBER: _ClassVar[int]
            currencyCode: str
            amount1000: int
            def __init__(self, currencyCode: _Optional[str] = ..., amount1000: _Optional[int] = ...) -> None: ...
        DEFAULT_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        DATETIME_FIELD_NUMBER: _ClassVar[int]
        default: str
        currency: HighlyStructuredMessage.HSMLocalizableParameter.HSMCurrency
        dateTime: HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime
        def __init__(self, default: _Optional[str] = ..., currency: _Optional[_Union[HighlyStructuredMessage.HSMLocalizableParameter.HSMCurrency, _Mapping]] = ..., dateTime: _Optional[_Union[HighlyStructuredMessage.HSMLocalizableParameter.HSMDateTime, _Mapping]] = ...) -> None: ...
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    ELEMENTNAME_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    FALLBACKLG_FIELD_NUMBER: _ClassVar[int]
    FALLBACKLC_FIELD_NUMBER: _ClassVar[int]
    LOCALIZABLEPARAMS_FIELD_NUMBER: _ClassVar[int]
    DETERMINISTICLG_FIELD_NUMBER: _ClassVar[int]
    DETERMINISTICLC_FIELD_NUMBER: _ClassVar[int]
    HYDRATEDHSM_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    elementName: str
    params: _containers.RepeatedScalarFieldContainer[str]
    fallbackLg: str
    fallbackLc: str
    localizableParams: _containers.RepeatedCompositeFieldContainer[HighlyStructuredMessage.HSMLocalizableParameter]
    deterministicLg: str
    deterministicLc: str
    hydratedHsm: TemplateMessage
    def __init__(self, namespace: _Optional[str] = ..., elementName: _Optional[str] = ..., params: _Optional[_Iterable[str]] = ..., fallbackLg: _Optional[str] = ..., fallbackLc: _Optional[str] = ..., localizableParams: _Optional[_Iterable[_Union[HighlyStructuredMessage.HSMLocalizableParameter, _Mapping]]] = ..., deterministicLg: _Optional[str] = ..., deterministicLc: _Optional[str] = ..., hydratedHsm: _Optional[_Union[TemplateMessage, _Mapping]] = ...) -> None: ...

class GroupInviteMessage(_message.Message):
    __slots__ = ["groupJid", "inviteCode", "inviteExpiration", "groupName", "jpegThumbnail", "caption", "contextInfo", "groupType"]
    class GroupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        DEFAULT: _ClassVar[GroupInviteMessage.GroupType]
        PARENT: _ClassVar[GroupInviteMessage.GroupType]
    DEFAULT: GroupInviteMessage.GroupType
    PARENT: GroupInviteMessage.GroupType
    GROUPJID_FIELD_NUMBER: _ClassVar[int]
    INVITECODE_FIELD_NUMBER: _ClassVar[int]
    INVITEEXPIRATION_FIELD_NUMBER: _ClassVar[int]
    GROUPNAME_FIELD_NUMBER: _ClassVar[int]
    JPEGTHUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    CAPTION_FIELD_NUMBER: _ClassVar[int]
    CONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    GROUPTYPE_FIELD_NUMBER: _ClassVar[int]
    groupJid: str
    inviteCode: str
    inviteExpiration: int
    groupName: str
    jpegThumbnail: bytes
    caption: str
    contextInfo: ContextInfo
    groupType: GroupInviteMessage.GroupType
    def __init__(self, groupJid: _Optional[str] = ..., inviteCode: _Optional[str] = ..., inviteExpiration: _Optional[int] = ..., groupName: _Optional[str] = ..., jpegThumbnail: _Optional[bytes] = ..., caption: _Optional[str] = ..., contextInfo: _Optional[_Union[ContextInfo, _Mapping]] = ..., groupType: _Optional[_Union[GroupInviteMessage.GroupType, str]] = ...) -> None: ...

class FutureProofMessage(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: Message
    def __init__(self, message: _Optional[_Union[Message, _Mapping]] = ...) -> None: ...

class ExtendedTextMessage(_message.Message):
    __slots__ = ["text", "matchedText", "canonicalUrl", "description", "title", "textArgb", "backgroundArgb", "font", "previewType", "jpegThumbnail", "contextInfo", "doNotPlayInline", "thumbnailDirectPath", "thumbnailSha256", "thumbnailEncSha256", "mediaKey", "mediaKeyTimestamp", "thumbnailHeight", "thumbnailWidth", "inviteLinkGroupType", "inviteLinkParentGroupSubjectV2", "inviteLinkParentGroupThumbnailV2", "inviteLinkGroupTypeV2", "viewOnce"]
    class PreviewType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        NONE: _ClassVar[ExtendedTextMessage.PreviewType]
        VIDEO: _ClassVar[ExtendedTextMessage.PreviewType]
    NONE: ExtendedTextMessage.PreviewType
    VIDEO: ExtendedTextMessage.PreviewType
    class InviteLinkGroupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        DEFAULT: _ClassVar[ExtendedTextMessage.InviteLinkGroupType]
        PARENT: _ClassVar[ExtendedTextMessage.InviteLinkGroupType]
        SUB: _ClassVar[ExtendedTextMessage.InviteLinkGroupType]
        DEFAULT_SUB: _ClassVar[ExtendedTextMessage.InviteLinkGroupType]
    DEFAULT: ExtendedTextMessage.InviteLinkGroupType
    PARENT: ExtendedTextMessage.InviteLinkGroupType
    SUB: ExtendedTextMessage.InviteLinkGroupType
    DEFAULT_SUB: ExtendedTextMessage.InviteLinkGroupType
    class FontType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        SANS_SERIF: _ClassVar[ExtendedTextMessage.FontType]
        SERIF: _ClassVar[ExtendedTextMessage.FontType]
        NORICAN_REGULAR: _ClassVar[ExtendedTextMessage.FontType]
        BRYNDAN_WRITE: _ClassVar[ExtendedTextMessage.FontType]
        BEBASNEUE_REGULAR: _ClassVar[ExtendedTextMessage.FontType]
        OSWALD_HEAVY: _ClassVar[ExtendedTextMessage.FontType]
        SYSTEM_BOLD: _ClassVar[ExtendedTextMessage.FontType]
        MORNINGBREEZE_REGULAR: _ClassVar[ExtendedTextMessage.FontType]
        CALISTOGA_REGULAR: _ClassVar[ExtendedTextMessage.FontType]
        EXO2_EXTRABOLD: _ClassVar[ExtendedTextMessage.FontType]
        COURIERPRIME_BOLD: _ClassVar[ExtendedTextMessage.FontType]
    SANS_SERIF: ExtendedTextMessage.FontType
    SERIF: ExtendedTextMessage.FontType
    NORICAN_REGULAR: ExtendedTextMessage.FontType
    BRYNDAN_WRITE: ExtendedTextMessage.FontType
    BEBASNEUE_REGULAR: ExtendedTextMessage.FontType
    OSWALD_HEAVY: ExtendedTextMessage.FontType
    SYSTEM_BOLD: ExtendedTextMessage.FontType
    MORNINGBREEZE_REGULAR: ExtendedTextMessage.FontType
    CALISTOGA_REGULAR: ExtendedTextMessage.FontType
    EXO2_EXTRABOLD: ExtendedTextMessage.FontType
    COURIERPRIME_BOLD: ExtendedTextMessage.FontType
    TEXT_FIELD_NUMBER: _ClassVar[int]
    MATCHEDTEXT_FIELD_NUMBER: _ClassVar[int]
    CANONICALURL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXTARGB_FIELD_NUMBER: _ClassVar[int]
    BACKGROUNDARGB_FIELD_NUMBER: _ClassVar[int]
    FONT_FIELD_NUMBER: _ClassVar[int]
    PREVIEWTYPE_FIELD_NUMBER: _ClassVar[int]
    JPEGTHUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    CONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    DONOTPLAYINLINE_FIELD_NUMBER: _ClassVar[int]
    THUMBNAILDIRECTPATH_FIELD_NUMBER: _ClassVar[int]
    THUMBNAILSHA256_FIELD_NUMBER: _ClassVar[int]
    THUMBNAILENCSHA256_FIELD_NUMBER: _ClassVar[int]
    MEDIAKEY_FIELD_NUMBER: _ClassVar[int]
    MEDIAKEYTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    THUMBNAILHEIGHT_FIELD_NUMBER: _ClassVar[int]
    THUMBNAILWIDTH_FIELD_NUMBER: _ClassVar[int]
    INVITELINKGROUPTYPE_FIELD_NUMBER: _ClassVar[int]
    INVITELINKPARENTGROUPSUBJECTV2_FIELD_NUMBER: _ClassVar[int]
    INVITELINKPARENTGROUPTHUMBNAILV2_FIELD_NUMBER: _ClassVar[int]
    INVITELINKGROUPTYPEV2_FIELD_NUMBER: _ClassVar[int]
    VIEWONCE_FIELD_NUMBER: _ClassVar[int]
    text: str
    matchedText: str
    canonicalUrl: str
    description: str
    title: str
    textArgb: int
    backgroundArgb: int
    font: ExtendedTextMessage.FontType
    previewType: ExtendedTextMessage.PreviewType
    jpegThumbnail: bytes
    contextInfo: ContextInfo
    doNotPlayInline: bool
    thumbnailDirectPath: str
    thumbnailSha256: bytes
    thumbnailEncSha256: bytes
    mediaKey: bytes
    mediaKeyTimestamp: int
    thumbnailHeight: int
    thumbnailWidth: int
    inviteLinkGroupType: ExtendedTextMessage.InviteLinkGroupType
    inviteLinkParentGroupSubjectV2: str
    inviteLinkParentGroupThumbnailV2: bytes
    inviteLinkGroupTypeV2: ExtendedTextMessage.InviteLinkGroupType
    viewOnce: bool
    def __init__(self, text: _Optional[str] = ..., matchedText: _Optional[str] = ..., canonicalUrl: _Optional[str] = ..., description: _Optional[str] = ..., title: _Optional[str] = ..., textArgb: _Optional[int] = ..., backgroundArgb: _Optional[int] = ..., font: _Optional[_Union[ExtendedTextMessage.FontType, str]] = ..., previewType: _Optional[_Union[ExtendedTextMessage.PreviewType, str]] = ..., jpegThumbnail: _Optional[bytes] = ..., contextInfo: _Optional[_Union[ContextInfo, _Mapping]] = ..., doNotPlayInline: bool = ..., thumbnailDirectPath: _Optional[str] = ..., thumbnailSha256: _Optional[bytes] = ..., thumbnailEncSha256: _Optional[bytes] = ..., mediaKey: _Optional[bytes] = ..., mediaKeyTimestamp: _Optional[int] = ..., thumbnailHeight: _Optional[int] = ..., thumbnailWidth: _Optional[int] = ..., inviteLinkGroupType: _Optional[_Union[ExtendedTextMessage.InviteLinkGroupType, str]] = ..., inviteLinkParentGroupSubjectV2: _Optional[str] = ..., inviteLinkParentGroupThumbnailV2: _Optional[bytes] = ..., inviteLinkGroupTypeV2: _Optional[_Union[ExtendedTextMessage.InviteLinkGroupType, str]] = ..., viewOnce: bool = ...) -> None: ...

class EncReactionMessage(_message.Message):
    __slots__ = ["targetMessageKey", "encPayload", "encIv"]
    TARGETMESSAGEKEY_FIELD_NUMBER: _ClassVar[int]
    ENCPAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ENCIV_FIELD_NUMBER: _ClassVar[int]
    targetMessageKey: MessageKey
    encPayload: bytes
    encIv: bytes
    def __init__(self, targetMessageKey: _Optional[_Union[MessageKey, _Mapping]] = ..., encPayload: _Optional[bytes] = ..., encIv: _Optional[bytes] = ...) -> None: ...

class DocumentMessage(_message.Message):
    __slots__ = ["url", "mimetype", "title", "fileSha256", "fileLength", "pageCount", "mediaKey", "fileName", "fileEncSha256", "directPath", "mediaKeyTimestamp", "contactVcard", "thumbnailDirectPath", "thumbnailSha256", "thumbnailEncSha256", "jpegThumbnail", "contextInfo", "thumbnailHeight", "thumbnailWidth", "caption"]
    URL_FIELD_NUMBER: _ClassVar[int]
    MIMETYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    FILESHA256_FIELD_NUMBER: _ClassVar[int]
    FILELENGTH_FIELD_NUMBER: _ClassVar[int]
    PAGECOUNT_FIELD_NUMBER: _ClassVar[int]
    MEDIAKEY_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FILEENCSHA256_FIELD_NUMBER: _ClassVar[int]
    DIRECTPATH_FIELD_NUMBER: _ClassVar[int]
    MEDIAKEYTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CONTACTVCARD_FIELD_NUMBER: _ClassVar[int]
    THUMBNAILDIRECTPATH_FIELD_NUMBER: _ClassVar[int]
    THUMBNAILSHA256_FIELD_NUMBER: _ClassVar[int]
    THUMBNAILENCSHA256_FIELD_NUMBER: _ClassVar[int]
    JPEGTHUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    CONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    THUMBNAILHEIGHT_FIELD_NUMBER: _ClassVar[int]
    THUMBNAILWIDTH_FIELD_NUMBER: _ClassVar[int]
    CAPTION_FIELD_NUMBER: _ClassVar[int]
    url: str
    mimetype: str
    title: str
    fileSha256: bytes
    fileLength: int
    pageCount: int
    mediaKey: bytes
    fileName: str
    fileEncSha256: bytes
    directPath: str
    mediaKeyTimestamp: int
    contactVcard: bool
    thumbnailDirectPath: str
    thumbnailSha256: bytes
    thumbnailEncSha256: bytes
    jpegThumbnail: bytes
    contextInfo: ContextInfo
    thumbnailHeight: int
    thumbnailWidth: int
    caption: str
    def __init__(self, url: _Optional[str] = ..., mimetype: _Optional[str] = ..., title: _Optional[str] = ..., fileSha256: _Optional[bytes] = ..., fileLength: _Optional[int] = ..., pageCount: _Optional[int] = ..., mediaKey: _Optional[bytes] = ..., fileName: _Optional[str] = ..., fileEncSha256: _Optional[bytes] = ..., directPath: _Optional[str] = ..., mediaKeyTimestamp: _Optional[int] = ..., contactVcard: bool = ..., thumbnailDirectPath: _Optional[str] = ..., thumbnailSha256: _Optional[bytes] = ..., thumbnailEncSha256: _Optional[bytes] = ..., jpegThumbnail: _Optional[bytes] = ..., contextInfo: _Optional[_Union[ContextInfo, _Mapping]] = ..., thumbnailHeight: _Optional[int] = ..., thumbnailWidth: _Optional[int] = ..., caption: _Optional[str] = ...) -> None: ...

class DeviceSentMessage(_message.Message):
    __slots__ = ["destinationJid", "message", "phash"]
    DESTINATIONJID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PHASH_FIELD_NUMBER: _ClassVar[int]
    destinationJid: str
    message: Message
    phash: str
    def __init__(self, destinationJid: _Optional[str] = ..., message: _Optional[_Union[Message, _Mapping]] = ..., phash: _Optional[str] = ...) -> None: ...

class DeclinePaymentRequestMessage(_message.Message):
    __slots__ = ["key"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: MessageKey
    def __init__(self, key: _Optional[_Union[MessageKey, _Mapping]] = ...) -> None: ...

class ContactsArrayMessage(_message.Message):
    __slots__ = ["displayName", "contacts", "contextInfo"]
    DISPLAYNAME_FIELD_NUMBER: _ClassVar[int]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    CONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    displayName: str
    contacts: _containers.RepeatedCompositeFieldContainer[ContactMessage]
    contextInfo: ContextInfo
    def __init__(self, displayName: _Optional[str] = ..., contacts: _Optional[_Iterable[_Union[ContactMessage, _Mapping]]] = ..., contextInfo: _Optional[_Union[ContextInfo, _Mapping]] = ...) -> None: ...

class ContactMessage(_message.Message):
    __slots__ = ["displayName", "vcard", "contextInfo"]
    DISPLAYNAME_FIELD_NUMBER: _ClassVar[int]
    VCARD_FIELD_NUMBER: _ClassVar[int]
    CONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    displayName: str
    vcard: str
    contextInfo: ContextInfo
    def __init__(self, displayName: _Optional[str] = ..., vcard: _Optional[str] = ..., contextInfo: _Optional[_Union[ContextInfo, _Mapping]] = ...) -> None: ...

class Chat(_message.Message):
    __slots__ = ["displayName", "id"]
    DISPLAYNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    displayName: str
    id: str
    def __init__(self, displayName: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class CancelPaymentRequestMessage(_message.Message):
    __slots__ = ["key"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: MessageKey
    def __init__(self, key: _Optional[_Union[MessageKey, _Mapping]] = ...) -> None: ...

class Call(_message.Message):
    __slots__ = ["callKey", "conversionSource", "conversionData", "conversionDelaySeconds"]
    CALLKEY_FIELD_NUMBER: _ClassVar[int]
    CONVERSIONSOURCE_FIELD_NUMBER: _ClassVar[int]
    CONVERSIONDATA_FIELD_NUMBER: _ClassVar[int]
    CONVERSIONDELAYSECONDS_FIELD_NUMBER: _ClassVar[int]
    callKey: bytes
    conversionSource: str
    conversionData: bytes
    conversionDelaySeconds: int
    def __init__(self, callKey: _Optional[bytes] = ..., conversionSource: _Optional[str] = ..., conversionData: _Optional[bytes] = ..., conversionDelaySeconds: _Optional[int] = ...) -> None: ...

class ButtonsResponseMessage(_message.Message):
    __slots__ = ["selectedButtonId", "contextInfo", "type", "selectedDisplayText"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[ButtonsResponseMessage.Type]
        DISPLAY_TEXT: _ClassVar[ButtonsResponseMessage.Type]
    UNKNOWN: ButtonsResponseMessage.Type
    DISPLAY_TEXT: ButtonsResponseMessage.Type
    SELECTEDBUTTONID_FIELD_NUMBER: _ClassVar[int]
    CONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SELECTEDDISPLAYTEXT_FIELD_NUMBER: _ClassVar[int]
    selectedButtonId: str
    contextInfo: ContextInfo
    type: ButtonsResponseMessage.Type
    selectedDisplayText: str
    def __init__(self, selectedButtonId: _Optional[str] = ..., contextInfo: _Optional[_Union[ContextInfo, _Mapping]] = ..., type: _Optional[_Union[ButtonsResponseMessage.Type, str]] = ..., selectedDisplayText: _Optional[str] = ...) -> None: ...

class ButtonsMessage(_message.Message):
    __slots__ = ["contentText", "footerText", "contextInfo", "buttons", "headerType", "text", "documentMessage", "imageMessage", "videoMessage", "locationMessage"]
    class HeaderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[ButtonsMessage.HeaderType]
        EMPTY: _ClassVar[ButtonsMessage.HeaderType]
        TEXT: _ClassVar[ButtonsMessage.HeaderType]
        DOCUMENT: _ClassVar[ButtonsMessage.HeaderType]
        IMAGE: _ClassVar[ButtonsMessage.HeaderType]
        VIDEO: _ClassVar[ButtonsMessage.HeaderType]
        LOCATION: _ClassVar[ButtonsMessage.HeaderType]
    UNKNOWN: ButtonsMessage.HeaderType
    EMPTY: ButtonsMessage.HeaderType
    TEXT: ButtonsMessage.HeaderType
    DOCUMENT: ButtonsMessage.HeaderType
    IMAGE: ButtonsMessage.HeaderType
    VIDEO: ButtonsMessage.HeaderType
    LOCATION: ButtonsMessage.HeaderType
    class Button(_message.Message):
        __slots__ = ["buttonId", "buttonText", "type", "nativeFlowInfo"]
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            UNKNOWN: _ClassVar[ButtonsMessage.Button.Type]
            RESPONSE: _ClassVar[ButtonsMessage.Button.Type]
            NATIVE_FLOW: _ClassVar[ButtonsMessage.Button.Type]
        UNKNOWN: ButtonsMessage.Button.Type
        RESPONSE: ButtonsMessage.Button.Type
        NATIVE_FLOW: ButtonsMessage.Button.Type
        class NativeFlowInfo(_message.Message):
            __slots__ = ["name", "paramsJson"]
            NAME_FIELD_NUMBER: _ClassVar[int]
            PARAMSJSON_FIELD_NUMBER: _ClassVar[int]
            name: str
            paramsJson: str
            def __init__(self, name: _Optional[str] = ..., paramsJson: _Optional[str] = ...) -> None: ...
        class ButtonText(_message.Message):
            __slots__ = ["displayText"]
            DISPLAYTEXT_FIELD_NUMBER: _ClassVar[int]
            displayText: str
            def __init__(self, displayText: _Optional[str] = ...) -> None: ...
        BUTTONID_FIELD_NUMBER: _ClassVar[int]
        BUTTONTEXT_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        NATIVEFLOWINFO_FIELD_NUMBER: _ClassVar[int]
        buttonId: str
        buttonText: ButtonsMessage.Button.ButtonText
        type: ButtonsMessage.Button.Type
        nativeFlowInfo: ButtonsMessage.Button.NativeFlowInfo
        def __init__(self, buttonId: _Optional[str] = ..., buttonText: _Optional[_Union[ButtonsMessage.Button.ButtonText, _Mapping]] = ..., type: _Optional[_Union[ButtonsMessage.Button.Type, str]] = ..., nativeFlowInfo: _Optional[_Union[ButtonsMessage.Button.NativeFlowInfo, _Mapping]] = ...) -> None: ...
    CONTENTTEXT_FIELD_NUMBER: _ClassVar[int]
    FOOTERTEXT_FIELD_NUMBER: _ClassVar[int]
    CONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    BUTTONS_FIELD_NUMBER: _ClassVar[int]
    HEADERTYPE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTMESSAGE_FIELD_NUMBER: _ClassVar[int]
    IMAGEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    VIDEOMESSAGE_FIELD_NUMBER: _ClassVar[int]
    LOCATIONMESSAGE_FIELD_NUMBER: _ClassVar[int]
    contentText: str
    footerText: str
    contextInfo: ContextInfo
    buttons: _containers.RepeatedCompositeFieldContainer[ButtonsMessage.Button]
    headerType: ButtonsMessage.HeaderType
    text: str
    documentMessage: DocumentMessage
    imageMessage: ImageMessage
    videoMessage: VideoMessage
    locationMessage: LocationMessage
    def __init__(self, contentText: _Optional[str] = ..., footerText: _Optional[str] = ..., contextInfo: _Optional[_Union[ContextInfo, _Mapping]] = ..., buttons: _Optional[_Iterable[_Union[ButtonsMessage.Button, _Mapping]]] = ..., headerType: _Optional[_Union[ButtonsMessage.HeaderType, str]] = ..., text: _Optional[str] = ..., documentMessage: _Optional[_Union[DocumentMessage, _Mapping]] = ..., imageMessage: _Optional[_Union[ImageMessage, _Mapping]] = ..., videoMessage: _Optional[_Union[VideoMessage, _Mapping]] = ..., locationMessage: _Optional[_Union[LocationMessage, _Mapping]] = ...) -> None: ...

class AudioMessage(_message.Message):
    __slots__ = ["url", "mimetype", "fileSha256", "fileLength", "seconds", "ptt", "mediaKey", "fileEncSha256", "directPath", "mediaKeyTimestamp", "contextInfo", "streamingSidecar", "waveform", "backgroundArgb", "viewOnce"]
    URL_FIELD_NUMBER: _ClassVar[int]
    MIMETYPE_FIELD_NUMBER: _ClassVar[int]
    FILESHA256_FIELD_NUMBER: _ClassVar[int]
    FILELENGTH_FIELD_NUMBER: _ClassVar[int]
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    PTT_FIELD_NUMBER: _ClassVar[int]
    MEDIAKEY_FIELD_NUMBER: _ClassVar[int]
    FILEENCSHA256_FIELD_NUMBER: _ClassVar[int]
    DIRECTPATH_FIELD_NUMBER: _ClassVar[int]
    MEDIAKEYTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    STREAMINGSIDECAR_FIELD_NUMBER: _ClassVar[int]
    WAVEFORM_FIELD_NUMBER: _ClassVar[int]
    BACKGROUNDARGB_FIELD_NUMBER: _ClassVar[int]
    VIEWONCE_FIELD_NUMBER: _ClassVar[int]
    url: str
    mimetype: str
    fileSha256: bytes
    fileLength: int
    seconds: int
    ptt: bool
    mediaKey: bytes
    fileEncSha256: bytes
    directPath: str
    mediaKeyTimestamp: int
    contextInfo: ContextInfo
    streamingSidecar: bytes
    waveform: bytes
    backgroundArgb: int
    viewOnce: bool
    def __init__(self, url: _Optional[str] = ..., mimetype: _Optional[str] = ..., fileSha256: _Optional[bytes] = ..., fileLength: _Optional[int] = ..., seconds: _Optional[int] = ..., ptt: bool = ..., mediaKey: _Optional[bytes] = ..., fileEncSha256: _Optional[bytes] = ..., directPath: _Optional[str] = ..., mediaKeyTimestamp: _Optional[int] = ..., contextInfo: _Optional[_Union[ContextInfo, _Mapping]] = ..., streamingSidecar: _Optional[bytes] = ..., waveform: _Optional[bytes] = ..., backgroundArgb: _Optional[int] = ..., viewOnce: bool = ...) -> None: ...

class AppStateSyncKey(_message.Message):
    __slots__ = ["keyId", "keyData"]
    KEYID_FIELD_NUMBER: _ClassVar[int]
    KEYDATA_FIELD_NUMBER: _ClassVar[int]
    keyId: AppStateSyncKeyId
    keyData: AppStateSyncKeyData
    def __init__(self, keyId: _Optional[_Union[AppStateSyncKeyId, _Mapping]] = ..., keyData: _Optional[_Union[AppStateSyncKeyData, _Mapping]] = ...) -> None: ...

class AppStateSyncKeyShare(_message.Message):
    __slots__ = ["keys"]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[AppStateSyncKey]
    def __init__(self, keys: _Optional[_Iterable[_Union[AppStateSyncKey, _Mapping]]] = ...) -> None: ...

class AppStateSyncKeyRequest(_message.Message):
    __slots__ = ["keyIds"]
    KEYIDS_FIELD_NUMBER: _ClassVar[int]
    keyIds: _containers.RepeatedCompositeFieldContainer[AppStateSyncKeyId]
    def __init__(self, keyIds: _Optional[_Iterable[_Union[AppStateSyncKeyId, _Mapping]]] = ...) -> None: ...

class AppStateSyncKeyId(_message.Message):
    __slots__ = ["keyId"]
    KEYID_FIELD_NUMBER: _ClassVar[int]
    keyId: bytes
    def __init__(self, keyId: _Optional[bytes] = ...) -> None: ...

class AppStateSyncKeyFingerprint(_message.Message):
    __slots__ = ["rawId", "currentIndex", "deviceIndexes"]
    RAWID_FIELD_NUMBER: _ClassVar[int]
    CURRENTINDEX_FIELD_NUMBER: _ClassVar[int]
    DEVICEINDEXES_FIELD_NUMBER: _ClassVar[int]
    rawId: int
    currentIndex: int
    deviceIndexes: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, rawId: _Optional[int] = ..., currentIndex: _Optional[int] = ..., deviceIndexes: _Optional[_Iterable[int]] = ...) -> None: ...

class AppStateSyncKeyData(_message.Message):
    __slots__ = ["keyData", "fingerprint", "timestamp"]
    KEYDATA_FIELD_NUMBER: _ClassVar[int]
    FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    keyData: bytes
    fingerprint: AppStateSyncKeyFingerprint
    timestamp: int
    def __init__(self, keyData: _Optional[bytes] = ..., fingerprint: _Optional[_Union[AppStateSyncKeyFingerprint, _Mapping]] = ..., timestamp: _Optional[int] = ...) -> None: ...

class AppStateFatalExceptionNotification(_message.Message):
    __slots__ = ["collectionNames", "timestamp"]
    COLLECTIONNAMES_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    collectionNames: _containers.RepeatedScalarFieldContainer[str]
    timestamp: int
    def __init__(self, collectionNames: _Optional[_Iterable[str]] = ..., timestamp: _Optional[int] = ...) -> None: ...

class Location(_message.Message):
    __slots__ = ["degreesLatitude", "degreesLongitude", "name"]
    DEGREESLATITUDE_FIELD_NUMBER: _ClassVar[int]
    DEGREESLONGITUDE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    degreesLatitude: float
    degreesLongitude: float
    name: str
    def __init__(self, degreesLatitude: _Optional[float] = ..., degreesLongitude: _Optional[float] = ..., name: _Optional[str] = ...) -> None: ...

class InteractiveAnnotation(_message.Message):
    __slots__ = ["polygonVertices", "location"]
    POLYGONVERTICES_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    polygonVertices: _containers.RepeatedCompositeFieldContainer[Point]
    location: Location
    def __init__(self, polygonVertices: _Optional[_Iterable[_Union[Point, _Mapping]]] = ..., location: _Optional[_Union[Location, _Mapping]] = ...) -> None: ...

class HydratedTemplateButton(_message.Message):
    __slots__ = ["index", "quickReplyButton", "urlButton", "callButton"]
    class HydratedURLButton(_message.Message):
        __slots__ = ["displayText", "url"]
        DISPLAYTEXT_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        displayText: str
        url: str
        def __init__(self, displayText: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
    class HydratedQuickReplyButton(_message.Message):
        __slots__ = ["displayText", "id"]
        DISPLAYTEXT_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        displayText: str
        id: str
        def __init__(self, displayText: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...
    class HydratedCallButton(_message.Message):
        __slots__ = ["displayText", "phoneNumber"]
        DISPLAYTEXT_FIELD_NUMBER: _ClassVar[int]
        PHONENUMBER_FIELD_NUMBER: _ClassVar[int]
        displayText: str
        phoneNumber: str
        def __init__(self, displayText: _Optional[str] = ..., phoneNumber: _Optional[str] = ...) -> None: ...
    INDEX_FIELD_NUMBER: _ClassVar[int]
    QUICKREPLYBUTTON_FIELD_NUMBER: _ClassVar[int]
    URLBUTTON_FIELD_NUMBER: _ClassVar[int]
    CALLBUTTON_FIELD_NUMBER: _ClassVar[int]
    index: int
    quickReplyButton: HydratedTemplateButton.HydratedQuickReplyButton
    urlButton: HydratedTemplateButton.HydratedURLButton
    callButton: HydratedTemplateButton.HydratedCallButton
    def __init__(self, index: _Optional[int] = ..., quickReplyButton: _Optional[_Union[HydratedTemplateButton.HydratedQuickReplyButton, _Mapping]] = ..., urlButton: _Optional[_Union[HydratedTemplateButton.HydratedURLButton, _Mapping]] = ..., callButton: _Optional[_Union[HydratedTemplateButton.HydratedCallButton, _Mapping]] = ...) -> None: ...

class GroupMention(_message.Message):
    __slots__ = ["groupJid", "groupSubject"]
    GROUPJID_FIELD_NUMBER: _ClassVar[int]
    GROUPSUBJECT_FIELD_NUMBER: _ClassVar[int]
    groupJid: str
    groupSubject: str
    def __init__(self, groupJid: _Optional[str] = ..., groupSubject: _Optional[str] = ...) -> None: ...

class DisappearingMode(_message.Message):
    __slots__ = ["initiator"]
    class Initiator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        CHANGED_IN_CHAT: _ClassVar[DisappearingMode.Initiator]
        INITIATED_BY_ME: _ClassVar[DisappearingMode.Initiator]
        INITIATED_BY_OTHER: _ClassVar[DisappearingMode.Initiator]
    CHANGED_IN_CHAT: DisappearingMode.Initiator
    INITIATED_BY_ME: DisappearingMode.Initiator
    INITIATED_BY_OTHER: DisappearingMode.Initiator
    INITIATOR_FIELD_NUMBER: _ClassVar[int]
    initiator: DisappearingMode.Initiator
    def __init__(self, initiator: _Optional[_Union[DisappearingMode.Initiator, str]] = ...) -> None: ...

class DeviceListMetadata(_message.Message):
    __slots__ = ["senderKeyHash", "senderTimestamp", "senderKeyIndexes", "recipientKeyHash", "recipientTimestamp", "recipientKeyIndexes"]
    SENDERKEYHASH_FIELD_NUMBER: _ClassVar[int]
    SENDERTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SENDERKEYINDEXES_FIELD_NUMBER: _ClassVar[int]
    RECIPIENTKEYHASH_FIELD_NUMBER: _ClassVar[int]
    RECIPIENTTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RECIPIENTKEYINDEXES_FIELD_NUMBER: _ClassVar[int]
    senderKeyHash: bytes
    senderTimestamp: int
    senderKeyIndexes: _containers.RepeatedScalarFieldContainer[int]
    recipientKeyHash: bytes
    recipientTimestamp: int
    recipientKeyIndexes: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, senderKeyHash: _Optional[bytes] = ..., senderTimestamp: _Optional[int] = ..., senderKeyIndexes: _Optional[_Iterable[int]] = ..., recipientKeyHash: _Optional[bytes] = ..., recipientTimestamp: _Optional[int] = ..., recipientKeyIndexes: _Optional[_Iterable[int]] = ...) -> None: ...

class ContextInfo(_message.Message):
    __slots__ = ["stanzaId", "participant", "quotedMessage", "remoteJid", "mentionedJid", "conversionSource", "conversionData", "conversionDelaySeconds", "forwardingScore", "isForwarded", "quotedAd", "placeholderKey", "expiration", "ephemeralSettingTimestamp", "ephemeralSharedSecret", "externalAdReply", "entryPointConversionSource", "entryPointConversionApp", "entryPointConversionDelaySeconds", "disappearingMode", "actionLink", "groupSubject", "parentGroupJid", "trustBannerType", "trustBannerAction", "isSampled", "groupMentions", "utm"]
    class UTMInfo(_message.Message):
        __slots__ = ["utmSource", "utmCampaign"]
        UTMSOURCE_FIELD_NUMBER: _ClassVar[int]
        UTMCAMPAIGN_FIELD_NUMBER: _ClassVar[int]
        utmSource: str
        utmCampaign: str
        def __init__(self, utmSource: _Optional[str] = ..., utmCampaign: _Optional[str] = ...) -> None: ...
    class ExternalAdReplyInfo(_message.Message):
        __slots__ = ["title", "body", "mediaType", "thumbnailUrl", "mediaUrl", "thumbnail", "sourceType", "sourceId", "sourceUrl", "containsAutoReply", "renderLargerThumbnail", "showAdAttribution", "ctwaClid"]
        class MediaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            NONE: _ClassVar[ContextInfo.ExternalAdReplyInfo.MediaType]
            IMAGE: _ClassVar[ContextInfo.ExternalAdReplyInfo.MediaType]
            VIDEO: _ClassVar[ContextInfo.ExternalAdReplyInfo.MediaType]
        NONE: ContextInfo.ExternalAdReplyInfo.MediaType
        IMAGE: ContextInfo.ExternalAdReplyInfo.MediaType
        VIDEO: ContextInfo.ExternalAdReplyInfo.MediaType
        TITLE_FIELD_NUMBER: _ClassVar[int]
        BODY_FIELD_NUMBER: _ClassVar[int]
        MEDIATYPE_FIELD_NUMBER: _ClassVar[int]
        THUMBNAILURL_FIELD_NUMBER: _ClassVar[int]
        MEDIAURL_FIELD_NUMBER: _ClassVar[int]
        THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
        SOURCETYPE_FIELD_NUMBER: _ClassVar[int]
        SOURCEID_FIELD_NUMBER: _ClassVar[int]
        SOURCEURL_FIELD_NUMBER: _ClassVar[int]
        CONTAINSAUTOREPLY_FIELD_NUMBER: _ClassVar[int]
        RENDERLARGERTHUMBNAIL_FIELD_NUMBER: _ClassVar[int]
        SHOWADATTRIBUTION_FIELD_NUMBER: _ClassVar[int]
        CTWACLID_FIELD_NUMBER: _ClassVar[int]
        title: str
        body: str
        mediaType: ContextInfo.ExternalAdReplyInfo.MediaType
        thumbnailUrl: str
        mediaUrl: str
        thumbnail: bytes
        sourceType: str
        sourceId: str
        sourceUrl: str
        containsAutoReply: bool
        renderLargerThumbnail: bool
        showAdAttribution: bool
        ctwaClid: str
        def __init__(self, title: _Optional[str] = ..., body: _Optional[str] = ..., mediaType: _Optional[_Union[ContextInfo.ExternalAdReplyInfo.MediaType, str]] = ..., thumbnailUrl: _Optional[str] = ..., mediaUrl: _Optional[str] = ..., thumbnail: _Optional[bytes] = ..., sourceType: _Optional[str] = ..., sourceId: _Optional[str] = ..., sourceUrl: _Optional[str] = ..., containsAutoReply: bool = ..., renderLargerThumbnail: bool = ..., showAdAttribution: bool = ..., ctwaClid: _Optional[str] = ...) -> None: ...
    class AdReplyInfo(_message.Message):
        __slots__ = ["advertiserName", "mediaType", "jpegThumbnail", "caption"]
        class MediaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            NONE: _ClassVar[ContextInfo.AdReplyInfo.MediaType]
            IMAGE: _ClassVar[ContextInfo.AdReplyInfo.MediaType]
            VIDEO: _ClassVar[ContextInfo.AdReplyInfo.MediaType]
        NONE: ContextInfo.AdReplyInfo.MediaType
        IMAGE: ContextInfo.AdReplyInfo.MediaType
        VIDEO: ContextInfo.AdReplyInfo.MediaType
        ADVERTISERNAME_FIELD_NUMBER: _ClassVar[int]
        MEDIATYPE_FIELD_NUMBER: _ClassVar[int]
        JPEGTHUMBNAIL_FIELD_NUMBER: _ClassVar[int]
        CAPTION_FIELD_NUMBER: _ClassVar[int]
        advertiserName: str
        mediaType: ContextInfo.AdReplyInfo.MediaType
        jpegThumbnail: bytes
        caption: str
        def __init__(self, advertiserName: _Optional[str] = ..., mediaType: _Optional[_Union[ContextInfo.AdReplyInfo.MediaType, str]] = ..., jpegThumbnail: _Optional[bytes] = ..., caption: _Optional[str] = ...) -> None: ...
    STANZAID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    QUOTEDMESSAGE_FIELD_NUMBER: _ClassVar[int]
    REMOTEJID_FIELD_NUMBER: _ClassVar[int]
    MENTIONEDJID_FIELD_NUMBER: _ClassVar[int]
    CONVERSIONSOURCE_FIELD_NUMBER: _ClassVar[int]
    CONVERSIONDATA_FIELD_NUMBER: _ClassVar[int]
    CONVERSIONDELAYSECONDS_FIELD_NUMBER: _ClassVar[int]
    FORWARDINGSCORE_FIELD_NUMBER: _ClassVar[int]
    ISFORWARDED_FIELD_NUMBER: _ClassVar[int]
    QUOTEDAD_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDERKEY_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    EPHEMERALSETTINGTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EPHEMERALSHAREDSECRET_FIELD_NUMBER: _ClassVar[int]
    EXTERNALADREPLY_FIELD_NUMBER: _ClassVar[int]
    ENTRYPOINTCONVERSIONSOURCE_FIELD_NUMBER: _ClassVar[int]
    ENTRYPOINTCONVERSIONAPP_FIELD_NUMBER: _ClassVar[int]
    ENTRYPOINTCONVERSIONDELAYSECONDS_FIELD_NUMBER: _ClassVar[int]
    DISAPPEARINGMODE_FIELD_NUMBER: _ClassVar[int]
    ACTIONLINK_FIELD_NUMBER: _ClassVar[int]
    GROUPSUBJECT_FIELD_NUMBER: _ClassVar[int]
    PARENTGROUPJID_FIELD_NUMBER: _ClassVar[int]
    TRUSTBANNERTYPE_FIELD_NUMBER: _ClassVar[int]
    TRUSTBANNERACTION_FIELD_NUMBER: _ClassVar[int]
    ISSAMPLED_FIELD_NUMBER: _ClassVar[int]
    GROUPMENTIONS_FIELD_NUMBER: _ClassVar[int]
    UTM_FIELD_NUMBER: _ClassVar[int]
    stanzaId: str
    participant: str
    quotedMessage: Message
    remoteJid: str
    mentionedJid: _containers.RepeatedScalarFieldContainer[str]
    conversionSource: str
    conversionData: bytes
    conversionDelaySeconds: int
    forwardingScore: int
    isForwarded: bool
    quotedAd: ContextInfo.AdReplyInfo
    placeholderKey: MessageKey
    expiration: int
    ephemeralSettingTimestamp: int
    ephemeralSharedSecret: bytes
    externalAdReply: ContextInfo.ExternalAdReplyInfo
    entryPointConversionSource: str
    entryPointConversionApp: str
    entryPointConversionDelaySeconds: int
    disappearingMode: DisappearingMode
    actionLink: ActionLink
    groupSubject: str
    parentGroupJid: str
    trustBannerType: str
    trustBannerAction: int
    isSampled: bool
    groupMentions: _containers.RepeatedCompositeFieldContainer[GroupMention]
    utm: ContextInfo.UTMInfo
    def __init__(self, stanzaId: _Optional[str] = ..., participant: _Optional[str] = ..., quotedMessage: _Optional[_Union[Message, _Mapping]] = ..., remoteJid: _Optional[str] = ..., mentionedJid: _Optional[_Iterable[str]] = ..., conversionSource: _Optional[str] = ..., conversionData: _Optional[bytes] = ..., conversionDelaySeconds: _Optional[int] = ..., forwardingScore: _Optional[int] = ..., isForwarded: bool = ..., quotedAd: _Optional[_Union[ContextInfo.AdReplyInfo, _Mapping]] = ..., placeholderKey: _Optional[_Union[MessageKey, _Mapping]] = ..., expiration: _Optional[int] = ..., ephemeralSettingTimestamp: _Optional[int] = ..., ephemeralSharedSecret: _Optional[bytes] = ..., externalAdReply: _Optional[_Union[ContextInfo.ExternalAdReplyInfo, _Mapping]] = ..., entryPointConversionSource: _Optional[str] = ..., entryPointConversionApp: _Optional[str] = ..., entryPointConversionDelaySeconds: _Optional[int] = ..., disappearingMode: _Optional[_Union[DisappearingMode, _Mapping]] = ..., actionLink: _Optional[_Union[ActionLink, _Mapping]] = ..., groupSubject: _Optional[str] = ..., parentGroupJid: _Optional[str] = ..., trustBannerType: _Optional[str] = ..., trustBannerAction: _Optional[int] = ..., isSampled: bool = ..., groupMentions: _Optional[_Iterable[_Union[GroupMention, _Mapping]]] = ..., utm: _Optional[_Union[ContextInfo.UTMInfo, _Mapping]] = ...) -> None: ...

class ActionLink(_message.Message):
    __slots__ = ["url", "buttonTitle"]
    URL_FIELD_NUMBER: _ClassVar[int]
    BUTTONTITLE_FIELD_NUMBER: _ClassVar[int]
    url: str
    buttonTitle: str
    def __init__(self, url: _Optional[str] = ..., buttonTitle: _Optional[str] = ...) -> None: ...

class TemplateButton(_message.Message):
    __slots__ = ["index", "quickReplyButton", "urlButton", "callButton"]
    class URLButton(_message.Message):
        __slots__ = ["displayText", "url"]
        DISPLAYTEXT_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        displayText: HighlyStructuredMessage
        url: HighlyStructuredMessage
        def __init__(self, displayText: _Optional[_Union[HighlyStructuredMessage, _Mapping]] = ..., url: _Optional[_Union[HighlyStructuredMessage, _Mapping]] = ...) -> None: ...
    class QuickReplyButton(_message.Message):
        __slots__ = ["displayText", "id"]
        DISPLAYTEXT_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        displayText: HighlyStructuredMessage
        id: str
        def __init__(self, displayText: _Optional[_Union[HighlyStructuredMessage, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...
    class CallButton(_message.Message):
        __slots__ = ["displayText", "phoneNumber"]
        DISPLAYTEXT_FIELD_NUMBER: _ClassVar[int]
        PHONENUMBER_FIELD_NUMBER: _ClassVar[int]
        displayText: HighlyStructuredMessage
        phoneNumber: HighlyStructuredMessage
        def __init__(self, displayText: _Optional[_Union[HighlyStructuredMessage, _Mapping]] = ..., phoneNumber: _Optional[_Union[HighlyStructuredMessage, _Mapping]] = ...) -> None: ...
    INDEX_FIELD_NUMBER: _ClassVar[int]
    QUICKREPLYBUTTON_FIELD_NUMBER: _ClassVar[int]
    URLBUTTON_FIELD_NUMBER: _ClassVar[int]
    CALLBUTTON_FIELD_NUMBER: _ClassVar[int]
    index: int
    quickReplyButton: TemplateButton.QuickReplyButton
    urlButton: TemplateButton.URLButton
    callButton: TemplateButton.CallButton
    def __init__(self, index: _Optional[int] = ..., quickReplyButton: _Optional[_Union[TemplateButton.QuickReplyButton, _Mapping]] = ..., urlButton: _Optional[_Union[TemplateButton.URLButton, _Mapping]] = ..., callButton: _Optional[_Union[TemplateButton.CallButton, _Mapping]] = ...) -> None: ...

class Point(_message.Message):
    __slots__ = ["xDeprecated", "yDeprecated", "x", "y"]
    XDEPRECATED_FIELD_NUMBER: _ClassVar[int]
    YDEPRECATED_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    xDeprecated: int
    yDeprecated: int
    x: float
    y: float
    def __init__(self, xDeprecated: _Optional[int] = ..., yDeprecated: _Optional[int] = ..., x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...

class PaymentBackground(_message.Message):
    __slots__ = ["id", "fileLength", "width", "height", "mimetype", "placeholderArgb", "textArgb", "subtextArgb", "mediaData", "type"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[PaymentBackground.Type]
        DEFAULT: _ClassVar[PaymentBackground.Type]
    UNKNOWN: PaymentBackground.Type
    DEFAULT: PaymentBackground.Type
    class MediaData(_message.Message):
        __slots__ = ["mediaKey", "mediaKeyTimestamp", "fileSha256", "fileEncSha256", "directPath"]
        MEDIAKEY_FIELD_NUMBER: _ClassVar[int]
        MEDIAKEYTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        FILESHA256_FIELD_NUMBER: _ClassVar[int]
        FILEENCSHA256_FIELD_NUMBER: _ClassVar[int]
        DIRECTPATH_FIELD_NUMBER: _ClassVar[int]
        mediaKey: bytes
        mediaKeyTimestamp: int
        fileSha256: bytes
        fileEncSha256: bytes
        directPath: str
        def __init__(self, mediaKey: _Optional[bytes] = ..., mediaKeyTimestamp: _Optional[int] = ..., fileSha256: _Optional[bytes] = ..., fileEncSha256: _Optional[bytes] = ..., directPath: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    FILELENGTH_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    MIMETYPE_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDERARGB_FIELD_NUMBER: _ClassVar[int]
    TEXTARGB_FIELD_NUMBER: _ClassVar[int]
    SUBTEXTARGB_FIELD_NUMBER: _ClassVar[int]
    MEDIADATA_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    fileLength: int
    width: int
    height: int
    mimetype: str
    placeholderArgb: int
    textArgb: int
    subtextArgb: int
    mediaData: PaymentBackground.MediaData
    type: PaymentBackground.Type
    def __init__(self, id: _Optional[str] = ..., fileLength: _Optional[int] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., mimetype: _Optional[str] = ..., placeholderArgb: _Optional[int] = ..., textArgb: _Optional[int] = ..., subtextArgb: _Optional[int] = ..., mediaData: _Optional[_Union[PaymentBackground.MediaData, _Mapping]] = ..., type: _Optional[_Union[PaymentBackground.Type, str]] = ...) -> None: ...

class Money(_message.Message):
    __slots__ = ["value", "offset", "currencyCode"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    CURRENCYCODE_FIELD_NUMBER: _ClassVar[int]
    value: int
    offset: int
    currencyCode: str
    def __init__(self, value: _Optional[int] = ..., offset: _Optional[int] = ..., currencyCode: _Optional[str] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ["conversation", "senderKeyDistributionMessage", "imageMessage", "contactMessage", "locationMessage", "extendedTextMessage", "documentMessage", "audioMessage", "videoMessage", "call", "chat", "protocolMessage", "contactsArrayMessage", "highlyStructuredMessage", "fastRatchetKeySenderKeyDistributionMessage", "sendPaymentMessage", "liveLocationMessage", "requestPaymentMessage", "declinePaymentRequestMessage", "cancelPaymentRequestMessage", "templateMessage", "stickerMessage", "groupInviteMessage", "templateButtonReplyMessage", "productMessage", "deviceSentMessage", "messageContextInfo", "listMessage", "viewOnceMessage", "orderMessage", "listResponseMessage", "ephemeralMessage", "invoiceMessage", "buttonsMessage", "buttonsResponseMessage", "paymentInviteMessage", "interactiveMessage", "reactionMessage", "stickerSyncRmrMessage", "interactiveResponseMessage", "pollCreationMessage", "pollUpdateMessage", "keepInChatMessage", "documentWithCaptionMessage", "requestPhoneNumberMessage", "viewOnceMessageV2", "encReactionMessage", "editedMessage", "viewOnceMessageV2Extension", "pollCreationMessageV2", "scheduledCallCreationMessage", "groupMentionedMessage", "pinMessage", "pollCreationMessageV3", "scheduledCallEditMessage", "ptvMessage"]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    SENDERKEYDISTRIBUTIONMESSAGE_FIELD_NUMBER: _ClassVar[int]
    IMAGEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTACTMESSAGE_FIELD_NUMBER: _ClassVar[int]
    LOCATIONMESSAGE_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDTEXTMESSAGE_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTMESSAGE_FIELD_NUMBER: _ClassVar[int]
    AUDIOMESSAGE_FIELD_NUMBER: _ClassVar[int]
    VIDEOMESSAGE_FIELD_NUMBER: _ClassVar[int]
    CALL_FIELD_NUMBER: _ClassVar[int]
    CHAT_FIELD_NUMBER: _ClassVar[int]
    PROTOCOLMESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTACTSARRAYMESSAGE_FIELD_NUMBER: _ClassVar[int]
    HIGHLYSTRUCTUREDMESSAGE_FIELD_NUMBER: _ClassVar[int]
    FASTRATCHETKEYSENDERKEYDISTRIBUTIONMESSAGE_FIELD_NUMBER: _ClassVar[int]
    SENDPAYMENTMESSAGE_FIELD_NUMBER: _ClassVar[int]
    LIVELOCATIONMESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTPAYMENTMESSAGE_FIELD_NUMBER: _ClassVar[int]
    DECLINEPAYMENTREQUESTMESSAGE_FIELD_NUMBER: _ClassVar[int]
    CANCELPAYMENTREQUESTMESSAGE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    STICKERMESSAGE_FIELD_NUMBER: _ClassVar[int]
    GROUPINVITEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATEBUTTONREPLYMESSAGE_FIELD_NUMBER: _ClassVar[int]
    PRODUCTMESSAGE_FIELD_NUMBER: _ClassVar[int]
    DEVICESENTMESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGECONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    LISTMESSAGE_FIELD_NUMBER: _ClassVar[int]
    VIEWONCEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    ORDERMESSAGE_FIELD_NUMBER: _ClassVar[int]
    LISTRESPONSEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    EPHEMERALMESSAGE_FIELD_NUMBER: _ClassVar[int]
    INVOICEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    BUTTONSMESSAGE_FIELD_NUMBER: _ClassVar[int]
    BUTTONSRESPONSEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    PAYMENTINVITEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    INTERACTIVEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    REACTIONMESSAGE_FIELD_NUMBER: _ClassVar[int]
    STICKERSYNCRMRMESSAGE_FIELD_NUMBER: _ClassVar[int]
    INTERACTIVERESPONSEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    POLLCREATIONMESSAGE_FIELD_NUMBER: _ClassVar[int]
    POLLUPDATEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    KEEPINCHATMESSAGE_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTWITHCAPTIONMESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTPHONENUMBERMESSAGE_FIELD_NUMBER: _ClassVar[int]
    VIEWONCEMESSAGEV2_FIELD_NUMBER: _ClassVar[int]
    ENCREACTIONMESSAGE_FIELD_NUMBER: _ClassVar[int]
    EDITEDMESSAGE_FIELD_NUMBER: _ClassVar[int]
    VIEWONCEMESSAGEV2EXTENSION_FIELD_NUMBER: _ClassVar[int]
    POLLCREATIONMESSAGEV2_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEDCALLCREATIONMESSAGE_FIELD_NUMBER: _ClassVar[int]
    GROUPMENTIONEDMESSAGE_FIELD_NUMBER: _ClassVar[int]
    PINMESSAGE_FIELD_NUMBER: _ClassVar[int]
    POLLCREATIONMESSAGEV3_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEDCALLEDITMESSAGE_FIELD_NUMBER: _ClassVar[int]
    PTVMESSAGE_FIELD_NUMBER: _ClassVar[int]
    conversation: str
    senderKeyDistributionMessage: SenderKeyDistributionMessage
    imageMessage: ImageMessage
    contactMessage: ContactMessage
    locationMessage: LocationMessage
    extendedTextMessage: ExtendedTextMessage
    documentMessage: DocumentMessage
    audioMessage: AudioMessage
    videoMessage: VideoMessage
    call: Call
    chat: Chat
    protocolMessage: ProtocolMessage
    contactsArrayMessage: ContactsArrayMessage
    highlyStructuredMessage: HighlyStructuredMessage
    fastRatchetKeySenderKeyDistributionMessage: SenderKeyDistributionMessage
    sendPaymentMessage: SendPaymentMessage
    liveLocationMessage: LiveLocationMessage
    requestPaymentMessage: RequestPaymentMessage
    declinePaymentRequestMessage: DeclinePaymentRequestMessage
    cancelPaymentRequestMessage: CancelPaymentRequestMessage
    templateMessage: TemplateMessage
    stickerMessage: StickerMessage
    groupInviteMessage: GroupInviteMessage
    templateButtonReplyMessage: TemplateButtonReplyMessage
    productMessage: ProductMessage
    deviceSentMessage: DeviceSentMessage
    messageContextInfo: MessageContextInfo
    listMessage: ListMessage
    viewOnceMessage: FutureProofMessage
    orderMessage: OrderMessage
    listResponseMessage: ListResponseMessage
    ephemeralMessage: FutureProofMessage
    invoiceMessage: InvoiceMessage
    buttonsMessage: ButtonsMessage
    buttonsResponseMessage: ButtonsResponseMessage
    paymentInviteMessage: PaymentInviteMessage
    interactiveMessage: InteractiveMessage
    reactionMessage: ReactionMessage
    stickerSyncRmrMessage: StickerSyncRMRMessage
    interactiveResponseMessage: InteractiveResponseMessage
    pollCreationMessage: PollCreationMessage
    pollUpdateMessage: PollUpdateMessage
    keepInChatMessage: KeepInChatMessage
    documentWithCaptionMessage: FutureProofMessage
    requestPhoneNumberMessage: RequestPhoneNumberMessage
    viewOnceMessageV2: FutureProofMessage
    encReactionMessage: EncReactionMessage
    editedMessage: FutureProofMessage
    viewOnceMessageV2Extension: FutureProofMessage
    pollCreationMessageV2: PollCreationMessage
    scheduledCallCreationMessage: ScheduledCallCreationMessage
    groupMentionedMessage: FutureProofMessage
    pinMessage: PinMessage
    pollCreationMessageV3: PollCreationMessage
    scheduledCallEditMessage: ScheduledCallEditMessage
    ptvMessage: VideoMessage
    def __init__(self, conversation: _Optional[str] = ..., senderKeyDistributionMessage: _Optional[_Union[SenderKeyDistributionMessage, _Mapping]] = ..., imageMessage: _Optional[_Union[ImageMessage, _Mapping]] = ..., contactMessage: _Optional[_Union[ContactMessage, _Mapping]] = ..., locationMessage: _Optional[_Union[LocationMessage, _Mapping]] = ..., extendedTextMessage: _Optional[_Union[ExtendedTextMessage, _Mapping]] = ..., documentMessage: _Optional[_Union[DocumentMessage, _Mapping]] = ..., audioMessage: _Optional[_Union[AudioMessage, _Mapping]] = ..., videoMessage: _Optional[_Union[VideoMessage, _Mapping]] = ..., call: _Optional[_Union[Call, _Mapping]] = ..., chat: _Optional[_Union[Chat, _Mapping]] = ..., protocolMessage: _Optional[_Union[ProtocolMessage, _Mapping]] = ..., contactsArrayMessage: _Optional[_Union[ContactsArrayMessage, _Mapping]] = ..., highlyStructuredMessage: _Optional[_Union[HighlyStructuredMessage, _Mapping]] = ..., fastRatchetKeySenderKeyDistributionMessage: _Optional[_Union[SenderKeyDistributionMessage, _Mapping]] = ..., sendPaymentMessage: _Optional[_Union[SendPaymentMessage, _Mapping]] = ..., liveLocationMessage: _Optional[_Union[LiveLocationMessage, _Mapping]] = ..., requestPaymentMessage: _Optional[_Union[RequestPaymentMessage, _Mapping]] = ..., declinePaymentRequestMessage: _Optional[_Union[DeclinePaymentRequestMessage, _Mapping]] = ..., cancelPaymentRequestMessage: _Optional[_Union[CancelPaymentRequestMessage, _Mapping]] = ..., templateMessage: _Optional[_Union[TemplateMessage, _Mapping]] = ..., stickerMessage: _Optional[_Union[StickerMessage, _Mapping]] = ..., groupInviteMessage: _Optional[_Union[GroupInviteMessage, _Mapping]] = ..., templateButtonReplyMessage: _Optional[_Union[TemplateButtonReplyMessage, _Mapping]] = ..., productMessage: _Optional[_Union[ProductMessage, _Mapping]] = ..., deviceSentMessage: _Optional[_Union[DeviceSentMessage, _Mapping]] = ..., messageContextInfo: _Optional[_Union[MessageContextInfo, _Mapping]] = ..., listMessage: _Optional[_Union[ListMessage, _Mapping]] = ..., viewOnceMessage: _Optional[_Union[FutureProofMessage, _Mapping]] = ..., orderMessage: _Optional[_Union[OrderMessage, _Mapping]] = ..., listResponseMessage: _Optional[_Union[ListResponseMessage, _Mapping]] = ..., ephemeralMessage: _Optional[_Union[FutureProofMessage, _Mapping]] = ..., invoiceMessage: _Optional[_Union[InvoiceMessage, _Mapping]] = ..., buttonsMessage: _Optional[_Union[ButtonsMessage, _Mapping]] = ..., buttonsResponseMessage: _Optional[_Union[ButtonsResponseMessage, _Mapping]] = ..., paymentInviteMessage: _Optional[_Union[PaymentInviteMessage, _Mapping]] = ..., interactiveMessage: _Optional[_Union[InteractiveMessage, _Mapping]] = ..., reactionMessage: _Optional[_Union[ReactionMessage, _Mapping]] = ..., stickerSyncRmrMessage: _Optional[_Union[StickerSyncRMRMessage, _Mapping]] = ..., interactiveResponseMessage: _Optional[_Union[InteractiveResponseMessage, _Mapping]] = ..., pollCreationMessage: _Optional[_Union[PollCreationMessage, _Mapping]] = ..., pollUpdateMessage: _Optional[_Union[PollUpdateMessage, _Mapping]] = ..., keepInChatMessage: _Optional[_Union[KeepInChatMessage, _Mapping]] = ..., documentWithCaptionMessage: _Optional[_Union[FutureProofMessage, _Mapping]] = ..., requestPhoneNumberMessage: _Optional[_Union[RequestPhoneNumberMessage, _Mapping]] = ..., viewOnceMessageV2: _Optional[_Union[FutureProofMessage, _Mapping]] = ..., encReactionMessage: _Optional[_Union[EncReactionMessage, _Mapping]] = ..., editedMessage: _Optional[_Union[FutureProofMessage, _Mapping]] = ..., viewOnceMessageV2Extension: _Optional[_Union[FutureProofMessage, _Mapping]] = ..., pollCreationMessageV2: _Optional[_Union[PollCreationMessage, _Mapping]] = ..., scheduledCallCreationMessage: _Optional[_Union[ScheduledCallCreationMessage, _Mapping]] = ..., groupMentionedMessage: _Optional[_Union[FutureProofMessage, _Mapping]] = ..., pinMessage: _Optional[_Union[PinMessage, _Mapping]] = ..., pollCreationMessageV3: _Optional[_Union[PollCreationMessage, _Mapping]] = ..., scheduledCallEditMessage: _Optional[_Union[ScheduledCallEditMessage, _Mapping]] = ..., ptvMessage: _Optional[_Union[VideoMessage, _Mapping]] = ...) -> None: ...

class MessageContextInfo(_message.Message):
    __slots__ = ["deviceListMetadata", "deviceListMetadataVersion", "messageSecret", "paddingBytes", "messageAddOnDurationInSecs"]
    DEVICELISTMETADATA_FIELD_NUMBER: _ClassVar[int]
    DEVICELISTMETADATAVERSION_FIELD_NUMBER: _ClassVar[int]
    MESSAGESECRET_FIELD_NUMBER: _ClassVar[int]
    PADDINGBYTES_FIELD_NUMBER: _ClassVar[int]
    MESSAGEADDONDURATIONINSECS_FIELD_NUMBER: _ClassVar[int]
    deviceListMetadata: DeviceListMetadata
    deviceListMetadataVersion: int
    messageSecret: bytes
    paddingBytes: bytes
    messageAddOnDurationInSecs: int
    def __init__(self, deviceListMetadata: _Optional[_Union[DeviceListMetadata, _Mapping]] = ..., deviceListMetadataVersion: _Optional[int] = ..., messageSecret: _Optional[bytes] = ..., paddingBytes: _Optional[bytes] = ..., messageAddOnDurationInSecs: _Optional[int] = ...) -> None: ...

class VideoMessage(_message.Message):
    __slots__ = ["url", "mimetype", "fileSha256", "fileLength", "seconds", "mediaKey", "caption", "gifPlayback", "height", "width", "fileEncSha256", "interactiveAnnotations", "directPath", "mediaKeyTimestamp", "jpegThumbnail", "contextInfo", "streamingSidecar", "gifAttribution", "viewOnce", "thumbnailDirectPath", "thumbnailSha256", "thumbnailEncSha256", "staticUrl"]
    class Attribution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        NONE: _ClassVar[VideoMessage.Attribution]
        GIPHY: _ClassVar[VideoMessage.Attribution]
        TENOR: _ClassVar[VideoMessage.Attribution]
    NONE: VideoMessage.Attribution
    GIPHY: VideoMessage.Attribution
    TENOR: VideoMessage.Attribution
    URL_FIELD_NUMBER: _ClassVar[int]
    MIMETYPE_FIELD_NUMBER: _ClassVar[int]
    FILESHA256_FIELD_NUMBER: _ClassVar[int]
    FILELENGTH_FIELD_NUMBER: _ClassVar[int]
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    MEDIAKEY_FIELD_NUMBER: _ClassVar[int]
    CAPTION_FIELD_NUMBER: _ClassVar[int]
    GIFPLAYBACK_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    FILEENCSHA256_FIELD_NUMBER: _ClassVar[int]
    INTERACTIVEANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    DIRECTPATH_FIELD_NUMBER: _ClassVar[int]
    MEDIAKEYTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    JPEGTHUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    CONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    STREAMINGSIDECAR_FIELD_NUMBER: _ClassVar[int]
    GIFATTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    VIEWONCE_FIELD_NUMBER: _ClassVar[int]
    THUMBNAILDIRECTPATH_FIELD_NUMBER: _ClassVar[int]
    THUMBNAILSHA256_FIELD_NUMBER: _ClassVar[int]
    THUMBNAILENCSHA256_FIELD_NUMBER: _ClassVar[int]
    STATICURL_FIELD_NUMBER: _ClassVar[int]
    url: str
    mimetype: str
    fileSha256: bytes
    fileLength: int
    seconds: int
    mediaKey: bytes
    caption: str
    gifPlayback: bool
    height: int
    width: int
    fileEncSha256: bytes
    interactiveAnnotations: _containers.RepeatedCompositeFieldContainer[InteractiveAnnotation]
    directPath: str
    mediaKeyTimestamp: int
    jpegThumbnail: bytes
    contextInfo: ContextInfo
    streamingSidecar: bytes
    gifAttribution: VideoMessage.Attribution
    viewOnce: bool
    thumbnailDirectPath: str
    thumbnailSha256: bytes
    thumbnailEncSha256: bytes
    staticUrl: str
    def __init__(self, url: _Optional[str] = ..., mimetype: _Optional[str] = ..., fileSha256: _Optional[bytes] = ..., fileLength: _Optional[int] = ..., seconds: _Optional[int] = ..., mediaKey: _Optional[bytes] = ..., caption: _Optional[str] = ..., gifPlayback: bool = ..., height: _Optional[int] = ..., width: _Optional[int] = ..., fileEncSha256: _Optional[bytes] = ..., interactiveAnnotations: _Optional[_Iterable[_Union[InteractiveAnnotation, _Mapping]]] = ..., directPath: _Optional[str] = ..., mediaKeyTimestamp: _Optional[int] = ..., jpegThumbnail: _Optional[bytes] = ..., contextInfo: _Optional[_Union[ContextInfo, _Mapping]] = ..., streamingSidecar: _Optional[bytes] = ..., gifAttribution: _Optional[_Union[VideoMessage.Attribution, str]] = ..., viewOnce: bool = ..., thumbnailDirectPath: _Optional[str] = ..., thumbnailSha256: _Optional[bytes] = ..., thumbnailEncSha256: _Optional[bytes] = ..., staticUrl: _Optional[str] = ...) -> None: ...

class TemplateMessage(_message.Message):
    __slots__ = ["contextInfo", "hydratedTemplate", "templateId", "fourRowTemplate", "hydratedFourRowTemplate", "interactiveMessageTemplate"]
    class HydratedFourRowTemplate(_message.Message):
        __slots__ = ["hydratedContentText", "hydratedFooterText", "hydratedButtons", "templateId", "documentMessage", "hydratedTitleText", "imageMessage", "videoMessage", "locationMessage"]
        HYDRATEDCONTENTTEXT_FIELD_NUMBER: _ClassVar[int]
        HYDRATEDFOOTERTEXT_FIELD_NUMBER: _ClassVar[int]
        HYDRATEDBUTTONS_FIELD_NUMBER: _ClassVar[int]
        TEMPLATEID_FIELD_NUMBER: _ClassVar[int]
        DOCUMENTMESSAGE_FIELD_NUMBER: _ClassVar[int]
        HYDRATEDTITLETEXT_FIELD_NUMBER: _ClassVar[int]
        IMAGEMESSAGE_FIELD_NUMBER: _ClassVar[int]
        VIDEOMESSAGE_FIELD_NUMBER: _ClassVar[int]
        LOCATIONMESSAGE_FIELD_NUMBER: _ClassVar[int]
        hydratedContentText: str
        hydratedFooterText: str
        hydratedButtons: _containers.RepeatedCompositeFieldContainer[HydratedTemplateButton]
        templateId: str
        documentMessage: DocumentMessage
        hydratedTitleText: str
        imageMessage: ImageMessage
        videoMessage: VideoMessage
        locationMessage: LocationMessage
        def __init__(self, hydratedContentText: _Optional[str] = ..., hydratedFooterText: _Optional[str] = ..., hydratedButtons: _Optional[_Iterable[_Union[HydratedTemplateButton, _Mapping]]] = ..., templateId: _Optional[str] = ..., documentMessage: _Optional[_Union[DocumentMessage, _Mapping]] = ..., hydratedTitleText: _Optional[str] = ..., imageMessage: _Optional[_Union[ImageMessage, _Mapping]] = ..., videoMessage: _Optional[_Union[VideoMessage, _Mapping]] = ..., locationMessage: _Optional[_Union[LocationMessage, _Mapping]] = ...) -> None: ...
    class FourRowTemplate(_message.Message):
        __slots__ = ["content", "footer", "buttons", "documentMessage", "highlyStructuredMessage", "imageMessage", "videoMessage", "locationMessage"]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        FOOTER_FIELD_NUMBER: _ClassVar[int]
        BUTTONS_FIELD_NUMBER: _ClassVar[int]
        DOCUMENTMESSAGE_FIELD_NUMBER: _ClassVar[int]
        HIGHLYSTRUCTUREDMESSAGE_FIELD_NUMBER: _ClassVar[int]
        IMAGEMESSAGE_FIELD_NUMBER: _ClassVar[int]
        VIDEOMESSAGE_FIELD_NUMBER: _ClassVar[int]
        LOCATIONMESSAGE_FIELD_NUMBER: _ClassVar[int]
        content: HighlyStructuredMessage
        footer: HighlyStructuredMessage
        buttons: _containers.RepeatedCompositeFieldContainer[TemplateButton]
        documentMessage: DocumentMessage
        highlyStructuredMessage: HighlyStructuredMessage
        imageMessage: ImageMessage
        videoMessage: VideoMessage
        locationMessage: LocationMessage
        def __init__(self, content: _Optional[_Union[HighlyStructuredMessage, _Mapping]] = ..., footer: _Optional[_Union[HighlyStructuredMessage, _Mapping]] = ..., buttons: _Optional[_Iterable[_Union[TemplateButton, _Mapping]]] = ..., documentMessage: _Optional[_Union[DocumentMessage, _Mapping]] = ..., highlyStructuredMessage: _Optional[_Union[HighlyStructuredMessage, _Mapping]] = ..., imageMessage: _Optional[_Union[ImageMessage, _Mapping]] = ..., videoMessage: _Optional[_Union[VideoMessage, _Mapping]] = ..., locationMessage: _Optional[_Union[LocationMessage, _Mapping]] = ...) -> None: ...
    CONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    HYDRATEDTEMPLATE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATEID_FIELD_NUMBER: _ClassVar[int]
    FOURROWTEMPLATE_FIELD_NUMBER: _ClassVar[int]
    HYDRATEDFOURROWTEMPLATE_FIELD_NUMBER: _ClassVar[int]
    INTERACTIVEMESSAGETEMPLATE_FIELD_NUMBER: _ClassVar[int]
    contextInfo: ContextInfo
    hydratedTemplate: TemplateMessage.HydratedFourRowTemplate
    templateId: str
    fourRowTemplate: TemplateMessage.FourRowTemplate
    hydratedFourRowTemplate: TemplateMessage.HydratedFourRowTemplate
    interactiveMessageTemplate: InteractiveMessage
    def __init__(self, contextInfo: _Optional[_Union[ContextInfo, _Mapping]] = ..., hydratedTemplate: _Optional[_Union[TemplateMessage.HydratedFourRowTemplate, _Mapping]] = ..., templateId: _Optional[str] = ..., fourRowTemplate: _Optional[_Union[TemplateMessage.FourRowTemplate, _Mapping]] = ..., hydratedFourRowTemplate: _Optional[_Union[TemplateMessage.HydratedFourRowTemplate, _Mapping]] = ..., interactiveMessageTemplate: _Optional[_Union[InteractiveMessage, _Mapping]] = ...) -> None: ...

class TemplateButtonReplyMessage(_message.Message):
    __slots__ = ["selectedId", "selectedDisplayText", "contextInfo", "selectedIndex"]
    SELECTEDID_FIELD_NUMBER: _ClassVar[int]
    SELECTEDDISPLAYTEXT_FIELD_NUMBER: _ClassVar[int]
    CONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    SELECTEDINDEX_FIELD_NUMBER: _ClassVar[int]
    selectedId: str
    selectedDisplayText: str
    contextInfo: ContextInfo
    selectedIndex: int
    def __init__(self, selectedId: _Optional[str] = ..., selectedDisplayText: _Optional[str] = ..., contextInfo: _Optional[_Union[ContextInfo, _Mapping]] = ..., selectedIndex: _Optional[int] = ...) -> None: ...

class StickerSyncRMRMessage(_message.Message):
    __slots__ = ["filehash", "rmrSource", "requestTimestamp"]
    FILEHASH_FIELD_NUMBER: _ClassVar[int]
    RMRSOURCE_FIELD_NUMBER: _ClassVar[int]
    REQUESTTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    filehash: _containers.RepeatedScalarFieldContainer[str]
    rmrSource: str
    requestTimestamp: int
    def __init__(self, filehash: _Optional[_Iterable[str]] = ..., rmrSource: _Optional[str] = ..., requestTimestamp: _Optional[int] = ...) -> None: ...

class StickerMessage(_message.Message):
    __slots__ = ["url", "fileSha256", "fileEncSha256", "mediaKey", "mimetype", "height", "width", "directPath", "fileLength", "mediaKeyTimestamp", "firstFrameLength", "firstFrameSidecar", "isAnimated", "pngThumbnail", "contextInfo", "stickerSentTs", "isAvatar"]
    URL_FIELD_NUMBER: _ClassVar[int]
    FILESHA256_FIELD_NUMBER: _ClassVar[int]
    FILEENCSHA256_FIELD_NUMBER: _ClassVar[int]
    MEDIAKEY_FIELD_NUMBER: _ClassVar[int]
    MIMETYPE_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    DIRECTPATH_FIELD_NUMBER: _ClassVar[int]
    FILELENGTH_FIELD_NUMBER: _ClassVar[int]
    MEDIAKEYTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    FIRSTFRAMELENGTH_FIELD_NUMBER: _ClassVar[int]
    FIRSTFRAMESIDECAR_FIELD_NUMBER: _ClassVar[int]
    ISANIMATED_FIELD_NUMBER: _ClassVar[int]
    PNGTHUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    CONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    STICKERSENTTS_FIELD_NUMBER: _ClassVar[int]
    ISAVATAR_FIELD_NUMBER: _ClassVar[int]
    url: str
    fileSha256: bytes
    fileEncSha256: bytes
    mediaKey: bytes
    mimetype: str
    height: int
    width: int
    directPath: str
    fileLength: int
    mediaKeyTimestamp: int
    firstFrameLength: int
    firstFrameSidecar: bytes
    isAnimated: bool
    pngThumbnail: bytes
    contextInfo: ContextInfo
    stickerSentTs: int
    isAvatar: bool
    def __init__(self, url: _Optional[str] = ..., fileSha256: _Optional[bytes] = ..., fileEncSha256: _Optional[bytes] = ..., mediaKey: _Optional[bytes] = ..., mimetype: _Optional[str] = ..., height: _Optional[int] = ..., width: _Optional[int] = ..., directPath: _Optional[str] = ..., fileLength: _Optional[int] = ..., mediaKeyTimestamp: _Optional[int] = ..., firstFrameLength: _Optional[int] = ..., firstFrameSidecar: _Optional[bytes] = ..., isAnimated: bool = ..., pngThumbnail: _Optional[bytes] = ..., contextInfo: _Optional[_Union[ContextInfo, _Mapping]] = ..., stickerSentTs: _Optional[int] = ..., isAvatar: bool = ...) -> None: ...

class SenderKeyDistributionMessage(_message.Message):
    __slots__ = ["groupId", "axolotlSenderKeyDistributionMessage"]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    AXOLOTLSENDERKEYDISTRIBUTIONMESSAGE_FIELD_NUMBER: _ClassVar[int]
    groupId: str
    axolotlSenderKeyDistributionMessage: bytes
    def __init__(self, groupId: _Optional[str] = ..., axolotlSenderKeyDistributionMessage: _Optional[bytes] = ...) -> None: ...

class SendPaymentMessage(_message.Message):
    __slots__ = ["noteMessage", "requestMessageKey", "background"]
    NOTEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTMESSAGEKEY_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    noteMessage: Message
    requestMessageKey: MessageKey
    background: PaymentBackground
    def __init__(self, noteMessage: _Optional[_Union[Message, _Mapping]] = ..., requestMessageKey: _Optional[_Union[MessageKey, _Mapping]] = ..., background: _Optional[_Union[PaymentBackground, _Mapping]] = ...) -> None: ...

class ScheduledCallEditMessage(_message.Message):
    __slots__ = ["key", "editType"]
    class EditType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[ScheduledCallEditMessage.EditType]
        CANCEL: _ClassVar[ScheduledCallEditMessage.EditType]
    UNKNOWN: ScheduledCallEditMessage.EditType
    CANCEL: ScheduledCallEditMessage.EditType
    KEY_FIELD_NUMBER: _ClassVar[int]
    EDITTYPE_FIELD_NUMBER: _ClassVar[int]
    key: MessageKey
    editType: ScheduledCallEditMessage.EditType
    def __init__(self, key: _Optional[_Union[MessageKey, _Mapping]] = ..., editType: _Optional[_Union[ScheduledCallEditMessage.EditType, str]] = ...) -> None: ...

class ScheduledCallCreationMessage(_message.Message):
    __slots__ = ["scheduledTimestampMs", "callType", "title"]
    class CallType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[ScheduledCallCreationMessage.CallType]
        VOICE: _ClassVar[ScheduledCallCreationMessage.CallType]
        VIDEO: _ClassVar[ScheduledCallCreationMessage.CallType]
    UNKNOWN: ScheduledCallCreationMessage.CallType
    VOICE: ScheduledCallCreationMessage.CallType
    VIDEO: ScheduledCallCreationMessage.CallType
    SCHEDULEDTIMESTAMPMS_FIELD_NUMBER: _ClassVar[int]
    CALLTYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    scheduledTimestampMs: int
    callType: ScheduledCallCreationMessage.CallType
    title: str
    def __init__(self, scheduledTimestampMs: _Optional[int] = ..., callType: _Optional[_Union[ScheduledCallCreationMessage.CallType, str]] = ..., title: _Optional[str] = ...) -> None: ...

class RequestPhoneNumberMessage(_message.Message):
    __slots__ = ["contextInfo"]
    CONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    contextInfo: ContextInfo
    def __init__(self, contextInfo: _Optional[_Union[ContextInfo, _Mapping]] = ...) -> None: ...

class RequestPaymentMessage(_message.Message):
    __slots__ = ["noteMessage", "currencyCodeIso4217", "amount1000", "requestFrom", "expiryTimestamp", "amount", "background"]
    NOTEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    CURRENCYCODEISO4217_FIELD_NUMBER: _ClassVar[int]
    AMOUNT1000_FIELD_NUMBER: _ClassVar[int]
    REQUESTFROM_FIELD_NUMBER: _ClassVar[int]
    EXPIRYTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    noteMessage: Message
    currencyCodeIso4217: str
    amount1000: int
    requestFrom: str
    expiryTimestamp: int
    amount: Money
    background: PaymentBackground
    def __init__(self, noteMessage: _Optional[_Union[Message, _Mapping]] = ..., currencyCodeIso4217: _Optional[str] = ..., amount1000: _Optional[int] = ..., requestFrom: _Optional[str] = ..., expiryTimestamp: _Optional[int] = ..., amount: _Optional[_Union[Money, _Mapping]] = ..., background: _Optional[_Union[PaymentBackground, _Mapping]] = ...) -> None: ...

class ReactionMessage(_message.Message):
    __slots__ = ["key", "text", "groupingKey", "senderTimestampMs"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    GROUPINGKEY_FIELD_NUMBER: _ClassVar[int]
    SENDERTIMESTAMPMS_FIELD_NUMBER: _ClassVar[int]
    key: MessageKey
    text: str
    groupingKey: str
    senderTimestampMs: int
    def __init__(self, key: _Optional[_Union[MessageKey, _Mapping]] = ..., text: _Optional[str] = ..., groupingKey: _Optional[str] = ..., senderTimestampMs: _Optional[int] = ...) -> None: ...

class ProtocolMessage(_message.Message):
    __slots__ = ["key", "type", "ephemeralExpiration", "ephemeralSettingTimestamp", "historySyncNotification", "appStateSyncKeyShare", "appStateSyncKeyRequest", "initialSecurityNotificationSettingSync", "appStateFatalExceptionNotification", "disappearingMode", "editedMessage", "timestampMs", "peerDataOperationRequestMessage", "peerDataOperationRequestResponseMessage"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        REVOKE: _ClassVar[ProtocolMessage.Type]
        EPHEMERAL_SETTING: _ClassVar[ProtocolMessage.Type]
        EPHEMERAL_SYNC_RESPONSE: _ClassVar[ProtocolMessage.Type]
        HISTORY_SYNC_NOTIFICATION: _ClassVar[ProtocolMessage.Type]
        APP_STATE_SYNC_KEY_SHARE: _ClassVar[ProtocolMessage.Type]
        APP_STATE_SYNC_KEY_REQUEST: _ClassVar[ProtocolMessage.Type]
        MSG_FANOUT_BACKFILL_REQUEST: _ClassVar[ProtocolMessage.Type]
        INITIAL_SECURITY_NOTIFICATION_SETTING_SYNC: _ClassVar[ProtocolMessage.Type]
        APP_STATE_FATAL_EXCEPTION_NOTIFICATION: _ClassVar[ProtocolMessage.Type]
        SHARE_PHONE_NUMBER: _ClassVar[ProtocolMessage.Type]
        MESSAGE_EDIT: _ClassVar[ProtocolMessage.Type]
        PEER_DATA_OPERATION_REQUEST_MESSAGE: _ClassVar[ProtocolMessage.Type]
        PEER_DATA_OPERATION_REQUEST_RESPONSE_MESSAGE: _ClassVar[ProtocolMessage.Type]
    REVOKE: ProtocolMessage.Type
    EPHEMERAL_SETTING: ProtocolMessage.Type
    EPHEMERAL_SYNC_RESPONSE: ProtocolMessage.Type
    HISTORY_SYNC_NOTIFICATION: ProtocolMessage.Type
    APP_STATE_SYNC_KEY_SHARE: ProtocolMessage.Type
    APP_STATE_SYNC_KEY_REQUEST: ProtocolMessage.Type
    MSG_FANOUT_BACKFILL_REQUEST: ProtocolMessage.Type
    INITIAL_SECURITY_NOTIFICATION_SETTING_SYNC: ProtocolMessage.Type
    APP_STATE_FATAL_EXCEPTION_NOTIFICATION: ProtocolMessage.Type
    SHARE_PHONE_NUMBER: ProtocolMessage.Type
    MESSAGE_EDIT: ProtocolMessage.Type
    PEER_DATA_OPERATION_REQUEST_MESSAGE: ProtocolMessage.Type
    PEER_DATA_OPERATION_REQUEST_RESPONSE_MESSAGE: ProtocolMessage.Type
    KEY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EPHEMERALEXPIRATION_FIELD_NUMBER: _ClassVar[int]
    EPHEMERALSETTINGTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HISTORYSYNCNOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    APPSTATESYNCKEYSHARE_FIELD_NUMBER: _ClassVar[int]
    APPSTATESYNCKEYREQUEST_FIELD_NUMBER: _ClassVar[int]
    INITIALSECURITYNOTIFICATIONSETTINGSYNC_FIELD_NUMBER: _ClassVar[int]
    APPSTATEFATALEXCEPTIONNOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    DISAPPEARINGMODE_FIELD_NUMBER: _ClassVar[int]
    EDITEDMESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPMS_FIELD_NUMBER: _ClassVar[int]
    PEERDATAOPERATIONREQUESTMESSAGE_FIELD_NUMBER: _ClassVar[int]
    PEERDATAOPERATIONREQUESTRESPONSEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    key: MessageKey
    type: ProtocolMessage.Type
    ephemeralExpiration: int
    ephemeralSettingTimestamp: int
    historySyncNotification: HistorySyncNotification
    appStateSyncKeyShare: AppStateSyncKeyShare
    appStateSyncKeyRequest: AppStateSyncKeyRequest
    initialSecurityNotificationSettingSync: InitialSecurityNotificationSettingSync
    appStateFatalExceptionNotification: AppStateFatalExceptionNotification
    disappearingMode: DisappearingMode
    editedMessage: Message
    timestampMs: int
    peerDataOperationRequestMessage: PeerDataOperationRequestMessage
    peerDataOperationRequestResponseMessage: PeerDataOperationRequestResponseMessage
    def __init__(self, key: _Optional[_Union[MessageKey, _Mapping]] = ..., type: _Optional[_Union[ProtocolMessage.Type, str]] = ..., ephemeralExpiration: _Optional[int] = ..., ephemeralSettingTimestamp: _Optional[int] = ..., historySyncNotification: _Optional[_Union[HistorySyncNotification, _Mapping]] = ..., appStateSyncKeyShare: _Optional[_Union[AppStateSyncKeyShare, _Mapping]] = ..., appStateSyncKeyRequest: _Optional[_Union[AppStateSyncKeyRequest, _Mapping]] = ..., initialSecurityNotificationSettingSync: _Optional[_Union[InitialSecurityNotificationSettingSync, _Mapping]] = ..., appStateFatalExceptionNotification: _Optional[_Union[AppStateFatalExceptionNotification, _Mapping]] = ..., disappearingMode: _Optional[_Union[DisappearingMode, _Mapping]] = ..., editedMessage: _Optional[_Union[Message, _Mapping]] = ..., timestampMs: _Optional[int] = ..., peerDataOperationRequestMessage: _Optional[_Union[PeerDataOperationRequestMessage, _Mapping]] = ..., peerDataOperationRequestResponseMessage: _Optional[_Union[PeerDataOperationRequestResponseMessage, _Mapping]] = ...) -> None: ...

class ProductMessage(_message.Message):
    __slots__ = ["product", "businessOwnerJid", "catalog", "body", "footer", "contextInfo"]
    class ProductSnapshot(_message.Message):
        __slots__ = ["productImage", "productId", "title", "description", "currencyCode", "priceAmount1000", "retailerId", "url", "productImageCount", "firstImageId", "salePriceAmount1000"]
        PRODUCTIMAGE_FIELD_NUMBER: _ClassVar[int]
        PRODUCTID_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        CURRENCYCODE_FIELD_NUMBER: _ClassVar[int]
        PRICEAMOUNT1000_FIELD_NUMBER: _ClassVar[int]
        RETAILERID_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        PRODUCTIMAGECOUNT_FIELD_NUMBER: _ClassVar[int]
        FIRSTIMAGEID_FIELD_NUMBER: _ClassVar[int]
        SALEPRICEAMOUNT1000_FIELD_NUMBER: _ClassVar[int]
        productImage: ImageMessage
        productId: str
        title: str
        description: str
        currencyCode: str
        priceAmount1000: int
        retailerId: str
        url: str
        productImageCount: int
        firstImageId: str
        salePriceAmount1000: int
        def __init__(self, productImage: _Optional[_Union[ImageMessage, _Mapping]] = ..., productId: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., currencyCode: _Optional[str] = ..., priceAmount1000: _Optional[int] = ..., retailerId: _Optional[str] = ..., url: _Optional[str] = ..., productImageCount: _Optional[int] = ..., firstImageId: _Optional[str] = ..., salePriceAmount1000: _Optional[int] = ...) -> None: ...
    class CatalogSnapshot(_message.Message):
        __slots__ = ["catalogImage", "title", "description"]
        CATALOGIMAGE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        catalogImage: ImageMessage
        title: str
        description: str
        def __init__(self, catalogImage: _Optional[_Union[ImageMessage, _Mapping]] = ..., title: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    BUSINESSOWNERJID_FIELD_NUMBER: _ClassVar[int]
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    FOOTER_FIELD_NUMBER: _ClassVar[int]
    CONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    product: ProductMessage.ProductSnapshot
    businessOwnerJid: str
    catalog: ProductMessage.CatalogSnapshot
    body: str
    footer: str
    contextInfo: ContextInfo
    def __init__(self, product: _Optional[_Union[ProductMessage.ProductSnapshot, _Mapping]] = ..., businessOwnerJid: _Optional[str] = ..., catalog: _Optional[_Union[ProductMessage.CatalogSnapshot, _Mapping]] = ..., body: _Optional[str] = ..., footer: _Optional[str] = ..., contextInfo: _Optional[_Union[ContextInfo, _Mapping]] = ...) -> None: ...

class PollVoteMessage(_message.Message):
    __slots__ = ["selectedOptions"]
    SELECTEDOPTIONS_FIELD_NUMBER: _ClassVar[int]
    selectedOptions: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, selectedOptions: _Optional[_Iterable[bytes]] = ...) -> None: ...

class PollUpdateMessage(_message.Message):
    __slots__ = ["pollCreationMessageKey", "vote", "metadata", "senderTimestampMs"]
    POLLCREATIONMESSAGEKEY_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SENDERTIMESTAMPMS_FIELD_NUMBER: _ClassVar[int]
    pollCreationMessageKey: MessageKey
    vote: PollEncValue
    metadata: PollUpdateMessageMetadata
    senderTimestampMs: int
    def __init__(self, pollCreationMessageKey: _Optional[_Union[MessageKey, _Mapping]] = ..., vote: _Optional[_Union[PollEncValue, _Mapping]] = ..., metadata: _Optional[_Union[PollUpdateMessageMetadata, _Mapping]] = ..., senderTimestampMs: _Optional[int] = ...) -> None: ...

class PollUpdateMessageMetadata(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PollEncValue(_message.Message):
    __slots__ = ["encPayload", "encIv"]
    ENCPAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ENCIV_FIELD_NUMBER: _ClassVar[int]
    encPayload: bytes
    encIv: bytes
    def __init__(self, encPayload: _Optional[bytes] = ..., encIv: _Optional[bytes] = ...) -> None: ...

class PollCreationMessage(_message.Message):
    __slots__ = ["encKey", "name", "options", "selectableOptionsCount", "contextInfo"]
    class Option(_message.Message):
        __slots__ = ["optionName"]
        OPTIONNAME_FIELD_NUMBER: _ClassVar[int]
        optionName: str
        def __init__(self, optionName: _Optional[str] = ...) -> None: ...
    ENCKEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SELECTABLEOPTIONSCOUNT_FIELD_NUMBER: _ClassVar[int]
    CONTEXTINFO_FIELD_NUMBER: _ClassVar[int]
    encKey: bytes
    name: str
    options: _containers.RepeatedCompositeFieldContainer[PollCreationMessage.Option]
    selectableOptionsCount: int
    contextInfo: ContextInfo
    def __init__(self, encKey: _Optional[bytes] = ..., name: _Optional[str] = ..., options: _Optional[_Iterable[_Union[PollCreationMessage.Option, _Mapping]]] = ..., selectableOptionsCount: _Optional[int] = ..., contextInfo: _Optional[_Union[ContextInfo, _Mapping]] = ...) -> None: ...

class PinMessage(_message.Message):
    __slots__ = ["key", "pinMessageType", "senderTimestampMs"]
    class PinMessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN_PIN_MESSAGE_TYPE: _ClassVar[PinMessage.PinMessageType]
        PIN_FOR_ALL: _ClassVar[PinMessage.PinMessageType]
        UNPIN_FOR_ALL: _ClassVar[PinMessage.PinMessageType]
    UNKNOWN_PIN_MESSAGE_TYPE: PinMessage.PinMessageType
    PIN_FOR_ALL: PinMessage.PinMessageType
    UNPIN_FOR_ALL: PinMessage.PinMessageType
    KEY_FIELD_NUMBER: _ClassVar[int]
    PINMESSAGETYPE_FIELD_NUMBER: _ClassVar[int]
    SENDERTIMESTAMPMS_FIELD_NUMBER: _ClassVar[int]
    key: MessageKey
    pinMessageType: PinMessage.PinMessageType
    senderTimestampMs: int
    def __init__(self, key: _Optional[_Union[MessageKey, _Mapping]] = ..., pinMessageType: _Optional[_Union[PinMessage.PinMessageType, str]] = ..., senderTimestampMs: _Optional[int] = ...) -> None: ...

class PeerDataOperationRequestResponseMessage(_message.Message):
    __slots__ = ["peerDataOperationRequestType", "stanzaId", "peerDataOperationResult"]
    class PeerDataOperationResult(_message.Message):
        __slots__ = ["mediaUploadResult", "stickerMessage", "linkPreviewResponse", "placeholderMessageResendResponse"]
        class PlaceholderMessageResendResponse(_message.Message):
            __slots__ = ["webMessageInfoBytes"]
            WEBMESSAGEINFOBYTES_FIELD_NUMBER: _ClassVar[int]
            webMessageInfoBytes: bytes
            def __init__(self, webMessageInfoBytes: _Optional[bytes] = ...) -> None: ...
        class LinkPreviewResponse(_message.Message):
            __slots__ = ["url", "title", "description", "thumbData", "canonicalUrl", "matchText", "previewType", "hqThumbnail"]
            class LinkPreviewHighQualityThumbnail(_message.Message):
                __slots__ = ["directPath", "thumbHash", "encThumbHash", "mediaKey", "mediaKeyTimestampMs", "thumbWidth", "thumbHeight"]
                DIRECTPATH_FIELD_NUMBER: _ClassVar[int]
                THUMBHASH_FIELD_NUMBER: _ClassVar[int]
                ENCTHUMBHASH_FIELD_NUMBER: _ClassVar[int]
                MEDIAKEY_FIELD_NUMBER: _ClassVar[int]
                MEDIAKEYTIMESTAMPMS_FIELD_NUMBER: _ClassVar[int]
                THUMBWIDTH_FIELD_NUMBER: _ClassVar[int]
                THUMBHEIGHT_FIELD_NUMBER: _ClassVar[int]
                directPath: str
                thumbHash: str
                encThumbHash: str
                mediaKey: bytes
                mediaKeyTimestampMs: int
                thumbWidth: int
                thumbHeight: int
                def __init__(self, directPath: _Optional[str] = ..., thumbHash: _Optional[str] = ..., encThumbHash: _Optional[str] = ..., mediaKey: _Optional[bytes] = ..., mediaKeyTimestampMs: _Optional[int] = ..., thumbWidth: _Optional[int] = ..., thumbHeight: _Optional[int] = ...) -> None: ...
            URL_FIELD_NUMBER: _ClassVar[int]
            TITLE_FIELD_NUMBER: _ClassVar[int]
            DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            THUMBDATA_FIELD_NUMBER: _ClassVar[int]
            CANONICALURL_FIELD_NUMBER: _ClassVar[int]
            MATCHTEXT_FIELD_NUMBER: _ClassVar[int]
            PREVIEWTYPE_FIELD_NUMBER: _ClassVar[int]
            HQTHUMBNAIL_FIELD_NUMBER: _ClassVar[int]
            url: str
            title: str
            description: str
            thumbData: bytes
            canonicalUrl: str
            matchText: str
            previewType: str
            hqThumbnail: PeerDataOperationRequestResponseMessage.PeerDataOperationResult.LinkPreviewResponse.LinkPreviewHighQualityThumbnail
            def __init__(self, url: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., thumbData: _Optional[bytes] = ..., canonicalUrl: _Optional[str] = ..., matchText: _Optional[str] = ..., previewType: _Optional[str] = ..., hqThumbnail: _Optional[_Union[PeerDataOperationRequestResponseMessage.PeerDataOperationResult.LinkPreviewResponse.LinkPreviewHighQualityThumbnail, _Mapping]] = ...) -> None: ...
        MEDIAUPLOADRESULT_FIELD_NUMBER: _ClassVar[int]
        STICKERMESSAGE_FIELD_NUMBER: _ClassVar[int]
        LINKPREVIEWRESPONSE_FIELD_NUMBER: _ClassVar[int]
        PLACEHOLDERMESSAGERESENDRESPONSE_FIELD_NUMBER: _ClassVar[int]
        mediaUploadResult: MediaRetryNotification.ResultType
        stickerMessage: StickerMessage
        linkPreviewResponse: PeerDataOperationRequestResponseMessage.PeerDataOperationResult.LinkPreviewResponse
        placeholderMessageResendResponse: PeerDataOperationRequestResponseMessage.PeerDataOperationResult.PlaceholderMessageResendResponse
        def __init__(self, mediaUploadResult: _Optional[_Union[MediaRetryNotification.ResultType, str]] = ..., stickerMessage: _Optional[_Union[StickerMessage, _Mapping]] = ..., linkPreviewResponse: _Optional[_Union[PeerDataOperationRequestResponseMessage.PeerDataOperationResult.LinkPreviewResponse, _Mapping]] = ..., placeholderMessageResendResponse: _Optional[_Union[PeerDataOperationRequestResponseMessage.PeerDataOperationResult.PlaceholderMessageResendResponse, _Mapping]] = ...) -> None: ...
    PEERDATAOPERATIONREQUESTTYPE_FIELD_NUMBER: _ClassVar[int]
    STANZAID_FIELD_NUMBER: _ClassVar[int]
    PEERDATAOPERATIONRESULT_FIELD_NUMBER: _ClassVar[int]
    peerDataOperationRequestType: PeerDataOperationRequestType
    stanzaId: str
    peerDataOperationResult: _containers.RepeatedCompositeFieldContainer[PeerDataOperationRequestResponseMessage.PeerDataOperationResult]
    def __init__(self, peerDataOperationRequestType: _Optional[_Union[PeerDataOperationRequestType, str]] = ..., stanzaId: _Optional[str] = ..., peerDataOperationResult: _Optional[_Iterable[_Union[PeerDataOperationRequestResponseMessage.PeerDataOperationResult, _Mapping]]] = ...) -> None: ...

class PeerDataOperationRequestMessage(_message.Message):
    __slots__ = ["peerDataOperationRequestType", "requestStickerReupload", "requestUrlPreview", "historySyncOnDemandRequest", "placeholderMessageResendRequest"]
    class RequestUrlPreview(_message.Message):
        __slots__ = ["url", "includeHqThumbnail"]
        URL_FIELD_NUMBER: _ClassVar[int]
        INCLUDEHQTHUMBNAIL_FIELD_NUMBER: _ClassVar[int]
        url: str
        includeHqThumbnail: bool
        def __init__(self, url: _Optional[str] = ..., includeHqThumbnail: bool = ...) -> None: ...
    class RequestStickerReupload(_message.Message):
        __slots__ = ["fileSha256"]
        FILESHA256_FIELD_NUMBER: _ClassVar[int]
        fileSha256: str
        def __init__(self, fileSha256: _Optional[str] = ...) -> None: ...
    class PlaceholderMessageResendRequest(_message.Message):
        __slots__ = ["messageKey"]
        MESSAGEKEY_FIELD_NUMBER: _ClassVar[int]
        messageKey: MessageKey
        def __init__(self, messageKey: _Optional[_Union[MessageKey, _Mapping]] = ...) -> None: ...
    class HistorySyncOnDemandRequest(_message.Message):
        __slots__ = ["chatJid", "oldestMsgId", "oldestMsgFromMe", "onDemandMsgCount", "oldestMsgTimestampMs"]
        CHATJID_FIELD_NUMBER: _ClassVar[int]
        OLDESTMSGID_FIELD_NUMBER: _ClassVar[int]
        OLDESTMSGFROMME_FIELD_NUMBER: _ClassVar[int]
        ONDEMANDMSGCOUNT_FIELD_NUMBER: _ClassVar[int]
        OLDESTMSGTIMESTAMPMS_FIELD_NUMBER: _ClassVar[int]
        chatJid: str
        oldestMsgId: str
        oldestMsgFromMe: bool
        onDemandMsgCount: int
        oldestMsgTimestampMs: int
        def __init__(self, chatJid: _Optional[str] = ..., oldestMsgId: _Optional[str] = ..., oldestMsgFromMe: bool = ..., onDemandMsgCount: _Optional[int] = ..., oldestMsgTimestampMs: _Optional[int] = ...) -> None: ...
    PEERDATAOPERATIONREQUESTTYPE_FIELD_NUMBER: _ClassVar[int]
    REQUESTSTICKERREUPLOAD_FIELD_NUMBER: _ClassVar[int]
    REQUESTURLPREVIEW_FIELD_NUMBER: _ClassVar[int]
    HISTORYSYNCONDEMANDREQUEST_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDERMESSAGERESENDREQUEST_FIELD_NUMBER: _ClassVar[int]
    peerDataOperationRequestType: PeerDataOperationRequestType
    requestStickerReupload: _containers.RepeatedCompositeFieldContainer[PeerDataOperationRequestMessage.RequestStickerReupload]
    requestUrlPreview: _containers.RepeatedCompositeFieldContainer[PeerDataOperationRequestMessage.RequestUrlPreview]
    historySyncOnDemandRequest: PeerDataOperationRequestMessage.HistorySyncOnDemandRequest
    placeholderMessageResendRequest: _containers.RepeatedCompositeFieldContainer[PeerDataOperationRequestMessage.PlaceholderMessageResendRequest]
    def __init__(self, peerDataOperationRequestType: _Optional[_Union[PeerDataOperationRequestType, str]] = ..., requestStickerReupload: _Optional[_Iterable[_Union[PeerDataOperationRequestMessage.RequestStickerReupload, _Mapping]]] = ..., requestUrlPreview: _Optional[_Iterable[_Union[PeerDataOperationRequestMessage.RequestUrlPreview, _Mapping]]] = ..., historySyncOnDemandRequest: _Optional[_Union[PeerDataOperationRequestMessage.HistorySyncOnDemandRequest, _Mapping]] = ..., placeholderMessageResendRequest: _Optional[_Iterable[_Union[PeerDataOperationRequestMessage.PlaceholderMessageResendRequest, _Mapping]]] = ...) -> None: ...

class EphemeralSetting(_message.Message):
    __slots__ = ["duration", "timestamp"]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    duration: int
    timestamp: int
    def __init__(self, duration: _Optional[int] = ..., timestamp: _Optional[int] = ...) -> None: ...

class WallpaperSettings(_message.Message):
    __slots__ = ["filename", "opacity"]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OPACITY_FIELD_NUMBER: _ClassVar[int]
    filename: str
    opacity: int
    def __init__(self, filename: _Optional[str] = ..., opacity: _Optional[int] = ...) -> None: ...

class StickerMetadata(_message.Message):
    __slots__ = ["url", "fileSha256", "fileEncSha256", "mediaKey", "mimetype", "height", "width", "directPath", "fileLength", "weight", "lastStickerSentTs"]
    URL_FIELD_NUMBER: _ClassVar[int]
    FILESHA256_FIELD_NUMBER: _ClassVar[int]
    FILEENCSHA256_FIELD_NUMBER: _ClassVar[int]
    MEDIAKEY_FIELD_NUMBER: _ClassVar[int]
    MIMETYPE_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    DIRECTPATH_FIELD_NUMBER: _ClassVar[int]
    FILELENGTH_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    LASTSTICKERSENTTS_FIELD_NUMBER: _ClassVar[int]
    url: str
    fileSha256: bytes
    fileEncSha256: bytes
    mediaKey: bytes
    mimetype: str
    height: int
    width: int
    directPath: str
    fileLength: int
    weight: float
    lastStickerSentTs: int
    def __init__(self, url: _Optional[str] = ..., fileSha256: _Optional[bytes] = ..., fileEncSha256: _Optional[bytes] = ..., mediaKey: _Optional[bytes] = ..., mimetype: _Optional[str] = ..., height: _Optional[int] = ..., width: _Optional[int] = ..., directPath: _Optional[str] = ..., fileLength: _Optional[int] = ..., weight: _Optional[float] = ..., lastStickerSentTs: _Optional[int] = ...) -> None: ...

class Pushname(_message.Message):
    __slots__ = ["id", "pushname"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PUSHNAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    pushname: str
    def __init__(self, id: _Optional[str] = ..., pushname: _Optional[str] = ...) -> None: ...

class PastParticipants(_message.Message):
    __slots__ = ["groupJid", "pastParticipants"]
    GROUPJID_FIELD_NUMBER: _ClassVar[int]
    PASTPARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    groupJid: str
    pastParticipants: _containers.RepeatedCompositeFieldContainer[PastParticipant]
    def __init__(self, groupJid: _Optional[str] = ..., pastParticipants: _Optional[_Iterable[_Union[PastParticipant, _Mapping]]] = ...) -> None: ...

class PastParticipant(_message.Message):
    __slots__ = ["userJid", "leaveReason", "leaveTs"]
    class LeaveReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        LEFT: _ClassVar[PastParticipant.LeaveReason]
        REMOVED: _ClassVar[PastParticipant.LeaveReason]
    LEFT: PastParticipant.LeaveReason
    REMOVED: PastParticipant.LeaveReason
    USERJID_FIELD_NUMBER: _ClassVar[int]
    LEAVEREASON_FIELD_NUMBER: _ClassVar[int]
    LEAVETS_FIELD_NUMBER: _ClassVar[int]
    userJid: str
    leaveReason: PastParticipant.LeaveReason
    leaveTs: int
    def __init__(self, userJid: _Optional[str] = ..., leaveReason: _Optional[_Union[PastParticipant.LeaveReason, str]] = ..., leaveTs: _Optional[int] = ...) -> None: ...

class NotificationSettings(_message.Message):
    __slots__ = ["messageVibrate", "messagePopup", "messageLight", "lowPriorityNotifications", "reactionsMuted", "callVibrate"]
    MESSAGEVIBRATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGEPOPUP_FIELD_NUMBER: _ClassVar[int]
    MESSAGELIGHT_FIELD_NUMBER: _ClassVar[int]
    LOWPRIORITYNOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    REACTIONSMUTED_FIELD_NUMBER: _ClassVar[int]
    CALLVIBRATE_FIELD_NUMBER: _ClassVar[int]
    messageVibrate: str
    messagePopup: str
    messageLight: str
    lowPriorityNotifications: bool
    reactionsMuted: bool
    callVibrate: str
    def __init__(self, messageVibrate: _Optional[str] = ..., messagePopup: _Optional[str] = ..., messageLight: _Optional[str] = ..., lowPriorityNotifications: bool = ..., reactionsMuted: bool = ..., callVibrate: _Optional[str] = ...) -> None: ...

class HistorySync(_message.Message):
    __slots__ = ["syncType", "conversations", "statusV3Messages", "chunkOrder", "progress", "pushnames", "globalSettings", "threadIdUserSecret", "threadDsTimeframeOffset", "recentStickers", "pastParticipants"]
    class HistorySyncType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        INITIAL_BOOTSTRAP: _ClassVar[HistorySync.HistorySyncType]
        INITIAL_STATUS_V3: _ClassVar[HistorySync.HistorySyncType]
        FULL: _ClassVar[HistorySync.HistorySyncType]
        RECENT: _ClassVar[HistorySync.HistorySyncType]
        PUSH_NAME: _ClassVar[HistorySync.HistorySyncType]
        NON_BLOCKING_DATA: _ClassVar[HistorySync.HistorySyncType]
        ON_DEMAND: _ClassVar[HistorySync.HistorySyncType]
    INITIAL_BOOTSTRAP: HistorySync.HistorySyncType
    INITIAL_STATUS_V3: HistorySync.HistorySyncType
    FULL: HistorySync.HistorySyncType
    RECENT: HistorySync.HistorySyncType
    PUSH_NAME: HistorySync.HistorySyncType
    NON_BLOCKING_DATA: HistorySync.HistorySyncType
    ON_DEMAND: HistorySync.HistorySyncType
    SYNCTYPE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATIONS_FIELD_NUMBER: _ClassVar[int]
    STATUSV3MESSAGES_FIELD_NUMBER: _ClassVar[int]
    CHUNKORDER_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    PUSHNAMES_FIELD_NUMBER: _ClassVar[int]
    GLOBALSETTINGS_FIELD_NUMBER: _ClassVar[int]
    THREADIDUSERSECRET_FIELD_NUMBER: _ClassVar[int]
    THREADDSTIMEFRAMEOFFSET_FIELD_NUMBER: _ClassVar[int]
    RECENTSTICKERS_FIELD_NUMBER: _ClassVar[int]
    PASTPARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    syncType: HistorySync.HistorySyncType
    conversations: _containers.RepeatedCompositeFieldContainer[Conversation]
    statusV3Messages: _containers.RepeatedCompositeFieldContainer[WebMessageInfo]
    chunkOrder: int
    progress: int
    pushnames: _containers.RepeatedCompositeFieldContainer[Pushname]
    globalSettings: GlobalSettings
    threadIdUserSecret: bytes
    threadDsTimeframeOffset: int
    recentStickers: _containers.RepeatedCompositeFieldContainer[StickerMetadata]
    pastParticipants: _containers.RepeatedCompositeFieldContainer[PastParticipants]
    def __init__(self, syncType: _Optional[_Union[HistorySync.HistorySyncType, str]] = ..., conversations: _Optional[_Iterable[_Union[Conversation, _Mapping]]] = ..., statusV3Messages: _Optional[_Iterable[_Union[WebMessageInfo, _Mapping]]] = ..., chunkOrder: _Optional[int] = ..., progress: _Optional[int] = ..., pushnames: _Optional[_Iterable[_Union[Pushname, _Mapping]]] = ..., globalSettings: _Optional[_Union[GlobalSettings, _Mapping]] = ..., threadIdUserSecret: _Optional[bytes] = ..., threadDsTimeframeOffset: _Optional[int] = ..., recentStickers: _Optional[_Iterable[_Union[StickerMetadata, _Mapping]]] = ..., pastParticipants: _Optional[_Iterable[_Union[PastParticipants, _Mapping]]] = ...) -> None: ...

class HistorySyncMsg(_message.Message):
    __slots__ = ["message", "msgOrderId"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MSGORDERID_FIELD_NUMBER: _ClassVar[int]
    message: WebMessageInfo
    msgOrderId: int
    def __init__(self, message: _Optional[_Union[WebMessageInfo, _Mapping]] = ..., msgOrderId: _Optional[int] = ...) -> None: ...

class GroupParticipant(_message.Message):
    __slots__ = ["userJid", "rank"]
    class Rank(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        REGULAR: _ClassVar[GroupParticipant.Rank]
        ADMIN: _ClassVar[GroupParticipant.Rank]
        SUPERADMIN: _ClassVar[GroupParticipant.Rank]
    REGULAR: GroupParticipant.Rank
    ADMIN: GroupParticipant.Rank
    SUPERADMIN: GroupParticipant.Rank
    USERJID_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    userJid: str
    rank: GroupParticipant.Rank
    def __init__(self, userJid: _Optional[str] = ..., rank: _Optional[_Union[GroupParticipant.Rank, str]] = ...) -> None: ...

class GlobalSettings(_message.Message):
    __slots__ = ["lightThemeWallpaper", "mediaVisibility", "darkThemeWallpaper", "autoDownloadWiFi", "autoDownloadCellular", "autoDownloadRoaming", "showIndividualNotificationsPreview", "showGroupNotificationsPreview", "disappearingModeDuration", "disappearingModeTimestamp", "avatarUserSettings", "fontSize", "securityNotifications", "autoUnarchiveChats", "videoQualityMode", "photoQualityMode", "individualNotificationSettings", "groupNotificationSettings"]
    LIGHTTHEMEWALLPAPER_FIELD_NUMBER: _ClassVar[int]
    MEDIAVISIBILITY_FIELD_NUMBER: _ClassVar[int]
    DARKTHEMEWALLPAPER_FIELD_NUMBER: _ClassVar[int]
    AUTODOWNLOADWIFI_FIELD_NUMBER: _ClassVar[int]
    AUTODOWNLOADCELLULAR_FIELD_NUMBER: _ClassVar[int]
    AUTODOWNLOADROAMING_FIELD_NUMBER: _ClassVar[int]
    SHOWINDIVIDUALNOTIFICATIONSPREVIEW_FIELD_NUMBER: _ClassVar[int]
    SHOWGROUPNOTIFICATIONSPREVIEW_FIELD_NUMBER: _ClassVar[int]
    DISAPPEARINGMODEDURATION_FIELD_NUMBER: _ClassVar[int]
    DISAPPEARINGMODETIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    AVATARUSERSETTINGS_FIELD_NUMBER: _ClassVar[int]
    FONTSIZE_FIELD_NUMBER: _ClassVar[int]
    SECURITYNOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    AUTOUNARCHIVECHATS_FIELD_NUMBER: _ClassVar[int]
    VIDEOQUALITYMODE_FIELD_NUMBER: _ClassVar[int]
    PHOTOQUALITYMODE_FIELD_NUMBER: _ClassVar[int]
    INDIVIDUALNOTIFICATIONSETTINGS_FIELD_NUMBER: _ClassVar[int]
    GROUPNOTIFICATIONSETTINGS_FIELD_NUMBER: _ClassVar[int]
    lightThemeWallpaper: WallpaperSettings
    mediaVisibility: MediaVisibility
    darkThemeWallpaper: WallpaperSettings
    autoDownloadWiFi: AutoDownloadSettings
    autoDownloadCellular: AutoDownloadSettings
    autoDownloadRoaming: AutoDownloadSettings
    showIndividualNotificationsPreview: bool
    showGroupNotificationsPreview: bool
    disappearingModeDuration: int
    disappearingModeTimestamp: int
    avatarUserSettings: AvatarUserSettings
    fontSize: int
    securityNotifications: bool
    autoUnarchiveChats: bool
    videoQualityMode: int
    photoQualityMode: int
    individualNotificationSettings: NotificationSettings
    groupNotificationSettings: NotificationSettings
    def __init__(self, lightThemeWallpaper: _Optional[_Union[WallpaperSettings, _Mapping]] = ..., mediaVisibility: _Optional[_Union[MediaVisibility, str]] = ..., darkThemeWallpaper: _Optional[_Union[WallpaperSettings, _Mapping]] = ..., autoDownloadWiFi: _Optional[_Union[AutoDownloadSettings, _Mapping]] = ..., autoDownloadCellular: _Optional[_Union[AutoDownloadSettings, _Mapping]] = ..., autoDownloadRoaming: _Optional[_Union[AutoDownloadSettings, _Mapping]] = ..., showIndividualNotificationsPreview: bool = ..., showGroupNotificationsPreview: bool = ..., disappearingModeDuration: _Optional[int] = ..., disappearingModeTimestamp: _Optional[int] = ..., avatarUserSettings: _Optional[_Union[AvatarUserSettings, _Mapping]] = ..., fontSize: _Optional[int] = ..., securityNotifications: bool = ..., autoUnarchiveChats: bool = ..., videoQualityMode: _Optional[int] = ..., photoQualityMode: _Optional[int] = ..., individualNotificationSettings: _Optional[_Union[NotificationSettings, _Mapping]] = ..., groupNotificationSettings: _Optional[_Union[NotificationSettings, _Mapping]] = ...) -> None: ...

class Conversation(_message.Message):
    __slots__ = ["id", "messages", "newJid", "oldJid", "lastMsgTimestamp", "unreadCount", "readOnly", "endOfHistoryTransfer", "ephemeralExpiration", "ephemeralSettingTimestamp", "endOfHistoryTransferType", "conversationTimestamp", "name", "pHash", "notSpam", "archived", "disappearingMode", "unreadMentionCount", "markedAsUnread", "participant", "tcToken", "tcTokenTimestamp", "contactPrimaryIdentityKey", "pinned", "muteEndTime", "wallpaper", "mediaVisibility", "tcTokenSenderTimestamp", "suspended", "terminated", "createdAt", "createdBy", "description", "support", "isParentGroup", "parentGroupId", "isDefaultSubgroup", "displayName", "pnJid", "shareOwnPn", "pnhDuplicateLidThread", "lidJid"]
    class EndOfHistoryTransferType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        COMPLETE_BUT_MORE_MESSAGES_REMAIN_ON_PRIMARY: _ClassVar[Conversation.EndOfHistoryTransferType]
        COMPLETE_AND_NO_MORE_MESSAGE_REMAIN_ON_PRIMARY: _ClassVar[Conversation.EndOfHistoryTransferType]
        COMPLETE_ON_DEMAND_SYNC_BUT_MORE_MSG_REMAIN_ON_PRIMARY: _ClassVar[Conversation.EndOfHistoryTransferType]
    COMPLETE_BUT_MORE_MESSAGES_REMAIN_ON_PRIMARY: Conversation.EndOfHistoryTransferType
    COMPLETE_AND_NO_MORE_MESSAGE_REMAIN_ON_PRIMARY: Conversation.EndOfHistoryTransferType
    COMPLETE_ON_DEMAND_SYNC_BUT_MORE_MSG_REMAIN_ON_PRIMARY: Conversation.EndOfHistoryTransferType
    ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    NEWJID_FIELD_NUMBER: _ClassVar[int]
    OLDJID_FIELD_NUMBER: _ClassVar[int]
    LASTMSGTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UNREADCOUNT_FIELD_NUMBER: _ClassVar[int]
    READONLY_FIELD_NUMBER: _ClassVar[int]
    ENDOFHISTORYTRANSFER_FIELD_NUMBER: _ClassVar[int]
    EPHEMERALEXPIRATION_FIELD_NUMBER: _ClassVar[int]
    EPHEMERALSETTINGTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ENDOFHISTORYTRANSFERTYPE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATIONTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHASH_FIELD_NUMBER: _ClassVar[int]
    NOTSPAM_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    DISAPPEARINGMODE_FIELD_NUMBER: _ClassVar[int]
    UNREADMENTIONCOUNT_FIELD_NUMBER: _ClassVar[int]
    MARKEDASUNREAD_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    TCTOKEN_FIELD_NUMBER: _ClassVar[int]
    TCTOKENTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CONTACTPRIMARYIDENTITYKEY_FIELD_NUMBER: _ClassVar[int]
    PINNED_FIELD_NUMBER: _ClassVar[int]
    MUTEENDTIME_FIELD_NUMBER: _ClassVar[int]
    WALLPAPER_FIELD_NUMBER: _ClassVar[int]
    MEDIAVISIBILITY_FIELD_NUMBER: _ClassVar[int]
    TCTOKENSENDERTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    TERMINATED_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    CREATEDBY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_FIELD_NUMBER: _ClassVar[int]
    ISPARENTGROUP_FIELD_NUMBER: _ClassVar[int]
    PARENTGROUPID_FIELD_NUMBER: _ClassVar[int]
    ISDEFAULTSUBGROUP_FIELD_NUMBER: _ClassVar[int]
    DISPLAYNAME_FIELD_NUMBER: _ClassVar[int]
    PNJID_FIELD_NUMBER: _ClassVar[int]
    SHAREOWNPN_FIELD_NUMBER: _ClassVar[int]
    PNHDUPLICATELIDTHREAD_FIELD_NUMBER: _ClassVar[int]
    LIDJID_FIELD_NUMBER: _ClassVar[int]
    id: str
    messages: _containers.RepeatedCompositeFieldContainer[HistorySyncMsg]
    newJid: str
    oldJid: str
    lastMsgTimestamp: int
    unreadCount: int
    readOnly: bool
    endOfHistoryTransfer: bool
    ephemeralExpiration: int
    ephemeralSettingTimestamp: int
    endOfHistoryTransferType: Conversation.EndOfHistoryTransferType
    conversationTimestamp: int
    name: str
    pHash: str
    notSpam: bool
    archived: bool
    disappearingMode: DisappearingMode
    unreadMentionCount: int
    markedAsUnread: bool
    participant: _containers.RepeatedCompositeFieldContainer[GroupParticipant]
    tcToken: bytes
    tcTokenTimestamp: int
    contactPrimaryIdentityKey: bytes
    pinned: int
    muteEndTime: int
    wallpaper: WallpaperSettings
    mediaVisibility: MediaVisibility
    tcTokenSenderTimestamp: int
    suspended: bool
    terminated: bool
    createdAt: int
    createdBy: str
    description: str
    support: bool
    isParentGroup: bool
    parentGroupId: str
    isDefaultSubgroup: bool
    displayName: str
    pnJid: str
    shareOwnPn: bool
    pnhDuplicateLidThread: bool
    lidJid: str
    def __init__(self, id: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[HistorySyncMsg, _Mapping]]] = ..., newJid: _Optional[str] = ..., oldJid: _Optional[str] = ..., lastMsgTimestamp: _Optional[int] = ..., unreadCount: _Optional[int] = ..., readOnly: bool = ..., endOfHistoryTransfer: bool = ..., ephemeralExpiration: _Optional[int] = ..., ephemeralSettingTimestamp: _Optional[int] = ..., endOfHistoryTransferType: _Optional[_Union[Conversation.EndOfHistoryTransferType, str]] = ..., conversationTimestamp: _Optional[int] = ..., name: _Optional[str] = ..., pHash: _Optional[str] = ..., notSpam: bool = ..., archived: bool = ..., disappearingMode: _Optional[_Union[DisappearingMode, _Mapping]] = ..., unreadMentionCount: _Optional[int] = ..., markedAsUnread: bool = ..., participant: _Optional[_Iterable[_Union[GroupParticipant, _Mapping]]] = ..., tcToken: _Optional[bytes] = ..., tcTokenTimestamp: _Optional[int] = ..., contactPrimaryIdentityKey: _Optional[bytes] = ..., pinned: _Optional[int] = ..., muteEndTime: _Optional[int] = ..., wallpaper: _Optional[_Union[WallpaperSettings, _Mapping]] = ..., mediaVisibility: _Optional[_Union[MediaVisibility, str]] = ..., tcTokenSenderTimestamp: _Optional[int] = ..., suspended: bool = ..., terminated: bool = ..., createdAt: _Optional[int] = ..., createdBy: _Optional[str] = ..., description: _Optional[str] = ..., support: bool = ..., isParentGroup: bool = ..., parentGroupId: _Optional[str] = ..., isDefaultSubgroup: bool = ..., displayName: _Optional[str] = ..., pnJid: _Optional[str] = ..., shareOwnPn: bool = ..., pnhDuplicateLidThread: bool = ..., lidJid: _Optional[str] = ...) -> None: ...

class AvatarUserSettings(_message.Message):
    __slots__ = ["fbid", "password"]
    FBID_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    fbid: str
    password: str
    def __init__(self, fbid: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class AutoDownloadSettings(_message.Message):
    __slots__ = ["downloadImages", "downloadAudio", "downloadVideo", "downloadDocuments"]
    DOWNLOADIMAGES_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADAUDIO_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADVIDEO_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADDOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    downloadImages: bool
    downloadAudio: bool
    downloadVideo: bool
    downloadDocuments: bool
    def __init__(self, downloadImages: bool = ..., downloadAudio: bool = ..., downloadVideo: bool = ..., downloadDocuments: bool = ...) -> None: ...

class MsgRowOpaqueData(_message.Message):
    __slots__ = ["currentMsg", "quotedMsg"]
    CURRENTMSG_FIELD_NUMBER: _ClassVar[int]
    QUOTEDMSG_FIELD_NUMBER: _ClassVar[int]
    currentMsg: MsgOpaqueData
    quotedMsg: MsgOpaqueData
    def __init__(self, currentMsg: _Optional[_Union[MsgOpaqueData, _Mapping]] = ..., quotedMsg: _Optional[_Union[MsgOpaqueData, _Mapping]] = ...) -> None: ...

class MsgOpaqueData(_message.Message):
    __slots__ = ["body", "caption", "lng", "isLive", "lat", "paymentAmount1000", "paymentNoteMsgBody", "canonicalUrl", "matchedText", "title", "description", "futureproofBuffer", "clientUrl", "loc", "pollName", "pollOptions", "pollSelectableOptionsCount", "messageSecret", "originalSelfAuthor", "senderTimestampMs", "pollUpdateParentKey", "encPollVote", "isSentCagPollCreation", "encReactionTargetMessageKey", "encReactionEncPayload", "encReactionEncIv"]
    class PollOption(_message.Message):
        __slots__ = ["name"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    CAPTION_FIELD_NUMBER: _ClassVar[int]
    LNG_FIELD_NUMBER: _ClassVar[int]
    ISLIVE_FIELD_NUMBER: _ClassVar[int]
    LAT_FIELD_NUMBER: _ClassVar[int]
    PAYMENTAMOUNT1000_FIELD_NUMBER: _ClassVar[int]
    PAYMENTNOTEMSGBODY_FIELD_NUMBER: _ClassVar[int]
    CANONICALURL_FIELD_NUMBER: _ClassVar[int]
    MATCHEDTEXT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FUTUREPROOFBUFFER_FIELD_NUMBER: _ClassVar[int]
    CLIENTURL_FIELD_NUMBER: _ClassVar[int]
    LOC_FIELD_NUMBER: _ClassVar[int]
    POLLNAME_FIELD_NUMBER: _ClassVar[int]
    POLLOPTIONS_FIELD_NUMBER: _ClassVar[int]
    POLLSELECTABLEOPTIONSCOUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGESECRET_FIELD_NUMBER: _ClassVar[int]
    ORIGINALSELFAUTHOR_FIELD_NUMBER: _ClassVar[int]
    SENDERTIMESTAMPMS_FIELD_NUMBER: _ClassVar[int]
    POLLUPDATEPARENTKEY_FIELD_NUMBER: _ClassVar[int]
    ENCPOLLVOTE_FIELD_NUMBER: _ClassVar[int]
    ISSENTCAGPOLLCREATION_FIELD_NUMBER: _ClassVar[int]
    ENCREACTIONTARGETMESSAGEKEY_FIELD_NUMBER: _ClassVar[int]
    ENCREACTIONENCPAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ENCREACTIONENCIV_FIELD_NUMBER: _ClassVar[int]
    body: str
    caption: str
    lng: float
    isLive: bool
    lat: float
    paymentAmount1000: int
    paymentNoteMsgBody: str
    canonicalUrl: str
    matchedText: str
    title: str
    description: str
    futureproofBuffer: bytes
    clientUrl: str
    loc: str
    pollName: str
    pollOptions: _containers.RepeatedCompositeFieldContainer[MsgOpaqueData.PollOption]
    pollSelectableOptionsCount: int
    messageSecret: bytes
    originalSelfAuthor: str
    senderTimestampMs: int
    pollUpdateParentKey: str
    encPollVote: PollEncValue
    isSentCagPollCreation: bool
    encReactionTargetMessageKey: str
    encReactionEncPayload: bytes
    encReactionEncIv: bytes
    def __init__(self, body: _Optional[str] = ..., caption: _Optional[str] = ..., lng: _Optional[float] = ..., isLive: bool = ..., lat: _Optional[float] = ..., paymentAmount1000: _Optional[int] = ..., paymentNoteMsgBody: _Optional[str] = ..., canonicalUrl: _Optional[str] = ..., matchedText: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., futureproofBuffer: _Optional[bytes] = ..., clientUrl: _Optional[str] = ..., loc: _Optional[str] = ..., pollName: _Optional[str] = ..., pollOptions: _Optional[_Iterable[_Union[MsgOpaqueData.PollOption, _Mapping]]] = ..., pollSelectableOptionsCount: _Optional[int] = ..., messageSecret: _Optional[bytes] = ..., originalSelfAuthor: _Optional[str] = ..., senderTimestampMs: _Optional[int] = ..., pollUpdateParentKey: _Optional[str] = ..., encPollVote: _Optional[_Union[PollEncValue, _Mapping]] = ..., isSentCagPollCreation: bool = ..., encReactionTargetMessageKey: _Optional[str] = ..., encReactionEncPayload: _Optional[bytes] = ..., encReactionEncIv: _Optional[bytes] = ...) -> None: ...

class ServerErrorReceipt(_message.Message):
    __slots__ = ["stanzaId"]
    STANZAID_FIELD_NUMBER: _ClassVar[int]
    stanzaId: str
    def __init__(self, stanzaId: _Optional[str] = ...) -> None: ...

class MediaRetryNotification(_message.Message):
    __slots__ = ["stanzaId", "directPath", "result"]
    class ResultType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        GENERAL_ERROR: _ClassVar[MediaRetryNotification.ResultType]
        SUCCESS: _ClassVar[MediaRetryNotification.ResultType]
        NOT_FOUND: _ClassVar[MediaRetryNotification.ResultType]
        DECRYPTION_ERROR: _ClassVar[MediaRetryNotification.ResultType]
    GENERAL_ERROR: MediaRetryNotification.ResultType
    SUCCESS: MediaRetryNotification.ResultType
    NOT_FOUND: MediaRetryNotification.ResultType
    DECRYPTION_ERROR: MediaRetryNotification.ResultType
    STANZAID_FIELD_NUMBER: _ClassVar[int]
    DIRECTPATH_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    stanzaId: str
    directPath: str
    result: MediaRetryNotification.ResultType
    def __init__(self, stanzaId: _Optional[str] = ..., directPath: _Optional[str] = ..., result: _Optional[_Union[MediaRetryNotification.ResultType, str]] = ...) -> None: ...

class MessageKey(_message.Message):
    __slots__ = ["remoteJid", "fromMe", "id", "participant"]
    REMOTEJID_FIELD_NUMBER: _ClassVar[int]
    FROMME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    remoteJid: str
    fromMe: bool
    id: str
    participant: str
    def __init__(self, remoteJid: _Optional[str] = ..., fromMe: bool = ..., id: _Optional[str] = ..., participant: _Optional[str] = ...) -> None: ...

class SyncdVersion(_message.Message):
    __slots__ = ["version"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    def __init__(self, version: _Optional[int] = ...) -> None: ...

class SyncdValue(_message.Message):
    __slots__ = ["blob"]
    BLOB_FIELD_NUMBER: _ClassVar[int]
    blob: bytes
    def __init__(self, blob: _Optional[bytes] = ...) -> None: ...

class SyncdSnapshot(_message.Message):
    __slots__ = ["version", "records", "mac", "keyId"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    MAC_FIELD_NUMBER: _ClassVar[int]
    KEYID_FIELD_NUMBER: _ClassVar[int]
    version: SyncdVersion
    records: _containers.RepeatedCompositeFieldContainer[SyncdRecord]
    mac: bytes
    keyId: KeyId
    def __init__(self, version: _Optional[_Union[SyncdVersion, _Mapping]] = ..., records: _Optional[_Iterable[_Union[SyncdRecord, _Mapping]]] = ..., mac: _Optional[bytes] = ..., keyId: _Optional[_Union[KeyId, _Mapping]] = ...) -> None: ...

class SyncdRecord(_message.Message):
    __slots__ = ["index", "value", "keyId"]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    KEYID_FIELD_NUMBER: _ClassVar[int]
    index: SyncdIndex
    value: SyncdValue
    keyId: KeyId
    def __init__(self, index: _Optional[_Union[SyncdIndex, _Mapping]] = ..., value: _Optional[_Union[SyncdValue, _Mapping]] = ..., keyId: _Optional[_Union[KeyId, _Mapping]] = ...) -> None: ...

class SyncdPatch(_message.Message):
    __slots__ = ["version", "mutations", "externalMutations", "snapshotMac", "patchMac", "keyId", "exitCode", "deviceIndex"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    MUTATIONS_FIELD_NUMBER: _ClassVar[int]
    EXTERNALMUTATIONS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOTMAC_FIELD_NUMBER: _ClassVar[int]
    PATCHMAC_FIELD_NUMBER: _ClassVar[int]
    KEYID_FIELD_NUMBER: _ClassVar[int]
    EXITCODE_FIELD_NUMBER: _ClassVar[int]
    DEVICEINDEX_FIELD_NUMBER: _ClassVar[int]
    version: SyncdVersion
    mutations: _containers.RepeatedCompositeFieldContainer[SyncdMutation]
    externalMutations: ExternalBlobReference
    snapshotMac: bytes
    patchMac: bytes
    keyId: KeyId
    exitCode: ExitCode
    deviceIndex: int
    def __init__(self, version: _Optional[_Union[SyncdVersion, _Mapping]] = ..., mutations: _Optional[_Iterable[_Union[SyncdMutation, _Mapping]]] = ..., externalMutations: _Optional[_Union[ExternalBlobReference, _Mapping]] = ..., snapshotMac: _Optional[bytes] = ..., patchMac: _Optional[bytes] = ..., keyId: _Optional[_Union[KeyId, _Mapping]] = ..., exitCode: _Optional[_Union[ExitCode, _Mapping]] = ..., deviceIndex: _Optional[int] = ...) -> None: ...

class SyncdMutations(_message.Message):
    __slots__ = ["mutations"]
    MUTATIONS_FIELD_NUMBER: _ClassVar[int]
    mutations: _containers.RepeatedCompositeFieldContainer[SyncdMutation]
    def __init__(self, mutations: _Optional[_Iterable[_Union[SyncdMutation, _Mapping]]] = ...) -> None: ...

class SyncdMutation(_message.Message):
    __slots__ = ["operation", "record"]
    class SyncdOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        SET: _ClassVar[SyncdMutation.SyncdOperation]
        REMOVE: _ClassVar[SyncdMutation.SyncdOperation]
    SET: SyncdMutation.SyncdOperation
    REMOVE: SyncdMutation.SyncdOperation
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    operation: SyncdMutation.SyncdOperation
    record: SyncdRecord
    def __init__(self, operation: _Optional[_Union[SyncdMutation.SyncdOperation, str]] = ..., record: _Optional[_Union[SyncdRecord, _Mapping]] = ...) -> None: ...

class SyncdIndex(_message.Message):
    __slots__ = ["blob"]
    BLOB_FIELD_NUMBER: _ClassVar[int]
    blob: bytes
    def __init__(self, blob: _Optional[bytes] = ...) -> None: ...

class KeyId(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class ExternalBlobReference(_message.Message):
    __slots__ = ["mediaKey", "directPath", "handle", "fileSizeBytes", "fileSha256", "fileEncSha256"]
    MEDIAKEY_FIELD_NUMBER: _ClassVar[int]
    DIRECTPATH_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    FILESIZEBYTES_FIELD_NUMBER: _ClassVar[int]
    FILESHA256_FIELD_NUMBER: _ClassVar[int]
    FILEENCSHA256_FIELD_NUMBER: _ClassVar[int]
    mediaKey: bytes
    directPath: str
    handle: str
    fileSizeBytes: int
    fileSha256: bytes
    fileEncSha256: bytes
    def __init__(self, mediaKey: _Optional[bytes] = ..., directPath: _Optional[str] = ..., handle: _Optional[str] = ..., fileSizeBytes: _Optional[int] = ..., fileSha256: _Optional[bytes] = ..., fileEncSha256: _Optional[bytes] = ...) -> None: ...

class ExitCode(_message.Message):
    __slots__ = ["code", "text"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    code: int
    text: str
    def __init__(self, code: _Optional[int] = ..., text: _Optional[str] = ...) -> None: ...

class SyncActionValue(_message.Message):
    __slots__ = ["timestamp", "starAction", "contactAction", "muteAction", "pinAction", "securityNotificationSetting", "pushNameSetting", "quickReplyAction", "recentEmojiWeightsAction", "labelEditAction", "labelAssociationAction", "localeSetting", "archiveChatAction", "deleteMessageForMeAction", "keyExpiration", "markChatAsReadAction", "clearChatAction", "deleteChatAction", "unarchiveChatsSetting", "primaryFeature", "androidUnsupportedActions", "agentAction", "subscriptionAction", "userStatusMuteAction", "timeFormatAction", "nuxAction", "primaryVersionAction", "stickerAction", "removeRecentStickerAction", "chatAssignment", "chatAssignmentOpenedStatus", "pnForLidChatAction", "marketingMessageAction", "marketingMessageBroadcastAction", "externalWebBetaAction"]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STARACTION_FIELD_NUMBER: _ClassVar[int]
    CONTACTACTION_FIELD_NUMBER: _ClassVar[int]
    MUTEACTION_FIELD_NUMBER: _ClassVar[int]
    PINACTION_FIELD_NUMBER: _ClassVar[int]
    SECURITYNOTIFICATIONSETTING_FIELD_NUMBER: _ClassVar[int]
    PUSHNAMESETTING_FIELD_NUMBER: _ClassVar[int]
    QUICKREPLYACTION_FIELD_NUMBER: _ClassVar[int]
    RECENTEMOJIWEIGHTSACTION_FIELD_NUMBER: _ClassVar[int]
    LABELEDITACTION_FIELD_NUMBER: _ClassVar[int]
    LABELASSOCIATIONACTION_FIELD_NUMBER: _ClassVar[int]
    LOCALESETTING_FIELD_NUMBER: _ClassVar[int]
    ARCHIVECHATACTION_FIELD_NUMBER: _ClassVar[int]
    DELETEMESSAGEFORMEACTION_FIELD_NUMBER: _ClassVar[int]
    KEYEXPIRATION_FIELD_NUMBER: _ClassVar[int]
    MARKCHATASREADACTION_FIELD_NUMBER: _ClassVar[int]
    CLEARCHATACTION_FIELD_NUMBER: _ClassVar[int]
    DELETECHATACTION_FIELD_NUMBER: _ClassVar[int]
    UNARCHIVECHATSSETTING_FIELD_NUMBER: _ClassVar[int]
    PRIMARYFEATURE_FIELD_NUMBER: _ClassVar[int]
    ANDROIDUNSUPPORTEDACTIONS_FIELD_NUMBER: _ClassVar[int]
    AGENTACTION_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONACTION_FIELD_NUMBER: _ClassVar[int]
    USERSTATUSMUTEACTION_FIELD_NUMBER: _ClassVar[int]
    TIMEFORMATACTION_FIELD_NUMBER: _ClassVar[int]
    NUXACTION_FIELD_NUMBER: _ClassVar[int]
    PRIMARYVERSIONACTION_FIELD_NUMBER: _ClassVar[int]
    STICKERACTION_FIELD_NUMBER: _ClassVar[int]
    REMOVERECENTSTICKERACTION_FIELD_NUMBER: _ClassVar[int]
    CHATASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    CHATASSIGNMENTOPENEDSTATUS_FIELD_NUMBER: _ClassVar[int]
    PNFORLIDCHATACTION_FIELD_NUMBER: _ClassVar[int]
    MARKETINGMESSAGEACTION_FIELD_NUMBER: _ClassVar[int]
    MARKETINGMESSAGEBROADCASTACTION_FIELD_NUMBER: _ClassVar[int]
    EXTERNALWEBBETAACTION_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    starAction: StarAction
    contactAction: ContactAction
    muteAction: MuteAction
    pinAction: PinAction
    securityNotificationSetting: SecurityNotificationSetting
    pushNameSetting: PushNameSetting
    quickReplyAction: QuickReplyAction
    recentEmojiWeightsAction: RecentEmojiWeightsAction
    labelEditAction: LabelEditAction
    labelAssociationAction: LabelAssociationAction
    localeSetting: LocaleSetting
    archiveChatAction: ArchiveChatAction
    deleteMessageForMeAction: DeleteMessageForMeAction
    keyExpiration: KeyExpiration
    markChatAsReadAction: MarkChatAsReadAction
    clearChatAction: ClearChatAction
    deleteChatAction: DeleteChatAction
    unarchiveChatsSetting: UnarchiveChatsSetting
    primaryFeature: PrimaryFeature
    androidUnsupportedActions: AndroidUnsupportedActions
    agentAction: AgentAction
    subscriptionAction: SubscriptionAction
    userStatusMuteAction: UserStatusMuteAction
    timeFormatAction: TimeFormatAction
    nuxAction: NuxAction
    primaryVersionAction: PrimaryVersionAction
    stickerAction: StickerAction
    removeRecentStickerAction: RemoveRecentStickerAction
    chatAssignment: ChatAssignmentAction
    chatAssignmentOpenedStatus: ChatAssignmentOpenedStatusAction
    pnForLidChatAction: PnForLidChatAction
    marketingMessageAction: MarketingMessageAction
    marketingMessageBroadcastAction: MarketingMessageBroadcastAction
    externalWebBetaAction: ExternalWebBetaAction
    def __init__(self, timestamp: _Optional[int] = ..., starAction: _Optional[_Union[StarAction, _Mapping]] = ..., contactAction: _Optional[_Union[ContactAction, _Mapping]] = ..., muteAction: _Optional[_Union[MuteAction, _Mapping]] = ..., pinAction: _Optional[_Union[PinAction, _Mapping]] = ..., securityNotificationSetting: _Optional[_Union[SecurityNotificationSetting, _Mapping]] = ..., pushNameSetting: _Optional[_Union[PushNameSetting, _Mapping]] = ..., quickReplyAction: _Optional[_Union[QuickReplyAction, _Mapping]] = ..., recentEmojiWeightsAction: _Optional[_Union[RecentEmojiWeightsAction, _Mapping]] = ..., labelEditAction: _Optional[_Union[LabelEditAction, _Mapping]] = ..., labelAssociationAction: _Optional[_Union[LabelAssociationAction, _Mapping]] = ..., localeSetting: _Optional[_Union[LocaleSetting, _Mapping]] = ..., archiveChatAction: _Optional[_Union[ArchiveChatAction, _Mapping]] = ..., deleteMessageForMeAction: _Optional[_Union[DeleteMessageForMeAction, _Mapping]] = ..., keyExpiration: _Optional[_Union[KeyExpiration, _Mapping]] = ..., markChatAsReadAction: _Optional[_Union[MarkChatAsReadAction, _Mapping]] = ..., clearChatAction: _Optional[_Union[ClearChatAction, _Mapping]] = ..., deleteChatAction: _Optional[_Union[DeleteChatAction, _Mapping]] = ..., unarchiveChatsSetting: _Optional[_Union[UnarchiveChatsSetting, _Mapping]] = ..., primaryFeature: _Optional[_Union[PrimaryFeature, _Mapping]] = ..., androidUnsupportedActions: _Optional[_Union[AndroidUnsupportedActions, _Mapping]] = ..., agentAction: _Optional[_Union[AgentAction, _Mapping]] = ..., subscriptionAction: _Optional[_Union[SubscriptionAction, _Mapping]] = ..., userStatusMuteAction: _Optional[_Union[UserStatusMuteAction, _Mapping]] = ..., timeFormatAction: _Optional[_Union[TimeFormatAction, _Mapping]] = ..., nuxAction: _Optional[_Union[NuxAction, _Mapping]] = ..., primaryVersionAction: _Optional[_Union[PrimaryVersionAction, _Mapping]] = ..., stickerAction: _Optional[_Union[StickerAction, _Mapping]] = ..., removeRecentStickerAction: _Optional[_Union[RemoveRecentStickerAction, _Mapping]] = ..., chatAssignment: _Optional[_Union[ChatAssignmentAction, _Mapping]] = ..., chatAssignmentOpenedStatus: _Optional[_Union[ChatAssignmentOpenedStatusAction, _Mapping]] = ..., pnForLidChatAction: _Optional[_Union[PnForLidChatAction, _Mapping]] = ..., marketingMessageAction: _Optional[_Union[MarketingMessageAction, _Mapping]] = ..., marketingMessageBroadcastAction: _Optional[_Union[MarketingMessageBroadcastAction, _Mapping]] = ..., externalWebBetaAction: _Optional[_Union[ExternalWebBetaAction, _Mapping]] = ...) -> None: ...

class UserStatusMuteAction(_message.Message):
    __slots__ = ["muted"]
    MUTED_FIELD_NUMBER: _ClassVar[int]
    muted: bool
    def __init__(self, muted: bool = ...) -> None: ...

class UnarchiveChatsSetting(_message.Message):
    __slots__ = ["unarchiveChats"]
    UNARCHIVECHATS_FIELD_NUMBER: _ClassVar[int]
    unarchiveChats: bool
    def __init__(self, unarchiveChats: bool = ...) -> None: ...

class TimeFormatAction(_message.Message):
    __slots__ = ["isTwentyFourHourFormatEnabled"]
    ISTWENTYFOURHOURFORMATENABLED_FIELD_NUMBER: _ClassVar[int]
    isTwentyFourHourFormatEnabled: bool
    def __init__(self, isTwentyFourHourFormatEnabled: bool = ...) -> None: ...

class SyncActionMessage(_message.Message):
    __slots__ = ["key", "timestamp"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    key: MessageKey
    timestamp: int
    def __init__(self, key: _Optional[_Union[MessageKey, _Mapping]] = ..., timestamp: _Optional[int] = ...) -> None: ...

class SyncActionMessageRange(_message.Message):
    __slots__ = ["lastMessageTimestamp", "lastSystemMessageTimestamp", "messages"]
    LASTMESSAGETIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LASTSYSTEMMESSAGETIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    lastMessageTimestamp: int
    lastSystemMessageTimestamp: int
    messages: _containers.RepeatedCompositeFieldContainer[SyncActionMessage]
    def __init__(self, lastMessageTimestamp: _Optional[int] = ..., lastSystemMessageTimestamp: _Optional[int] = ..., messages: _Optional[_Iterable[_Union[SyncActionMessage, _Mapping]]] = ...) -> None: ...

class SubscriptionAction(_message.Message):
    __slots__ = ["isDeactivated", "isAutoRenewing", "expirationDate"]
    ISDEACTIVATED_FIELD_NUMBER: _ClassVar[int]
    ISAUTORENEWING_FIELD_NUMBER: _ClassVar[int]
    EXPIRATIONDATE_FIELD_NUMBER: _ClassVar[int]
    isDeactivated: bool
    isAutoRenewing: bool
    expirationDate: int
    def __init__(self, isDeactivated: bool = ..., isAutoRenewing: bool = ..., expirationDate: _Optional[int] = ...) -> None: ...

class StickerAction(_message.Message):
    __slots__ = ["url", "fileEncSha256", "mediaKey", "mimetype", "height", "width", "directPath", "fileLength", "isFavorite", "deviceIdHint"]
    URL_FIELD_NUMBER: _ClassVar[int]
    FILEENCSHA256_FIELD_NUMBER: _ClassVar[int]
    MEDIAKEY_FIELD_NUMBER: _ClassVar[int]
    MIMETYPE_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    DIRECTPATH_FIELD_NUMBER: _ClassVar[int]
    FILELENGTH_FIELD_NUMBER: _ClassVar[int]
    ISFAVORITE_FIELD_NUMBER: _ClassVar[int]
    DEVICEIDHINT_FIELD_NUMBER: _ClassVar[int]
    url: str
    fileEncSha256: bytes
    mediaKey: bytes
    mimetype: str
    height: int
    width: int
    directPath: str
    fileLength: int
    isFavorite: bool
    deviceIdHint: int
    def __init__(self, url: _Optional[str] = ..., fileEncSha256: _Optional[bytes] = ..., mediaKey: _Optional[bytes] = ..., mimetype: _Optional[str] = ..., height: _Optional[int] = ..., width: _Optional[int] = ..., directPath: _Optional[str] = ..., fileLength: _Optional[int] = ..., isFavorite: bool = ..., deviceIdHint: _Optional[int] = ...) -> None: ...

class StarAction(_message.Message):
    __slots__ = ["starred"]
    STARRED_FIELD_NUMBER: _ClassVar[int]
    starred: bool
    def __init__(self, starred: bool = ...) -> None: ...

class SecurityNotificationSetting(_message.Message):
    __slots__ = ["showNotification"]
    SHOWNOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    showNotification: bool
    def __init__(self, showNotification: bool = ...) -> None: ...

class RemoveRecentStickerAction(_message.Message):
    __slots__ = ["lastStickerSentTs"]
    LASTSTICKERSENTTS_FIELD_NUMBER: _ClassVar[int]
    lastStickerSentTs: int
    def __init__(self, lastStickerSentTs: _Optional[int] = ...) -> None: ...

class RecentEmojiWeightsAction(_message.Message):
    __slots__ = ["weights"]
    WEIGHTS_FIELD_NUMBER: _ClassVar[int]
    weights: _containers.RepeatedCompositeFieldContainer[RecentEmojiWeight]
    def __init__(self, weights: _Optional[_Iterable[_Union[RecentEmojiWeight, _Mapping]]] = ...) -> None: ...

class QuickReplyAction(_message.Message):
    __slots__ = ["shortcut", "message", "keywords", "count", "deleted"]
    SHORTCUT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    shortcut: str
    message: str
    keywords: _containers.RepeatedScalarFieldContainer[str]
    count: int
    deleted: bool
    def __init__(self, shortcut: _Optional[str] = ..., message: _Optional[str] = ..., keywords: _Optional[_Iterable[str]] = ..., count: _Optional[int] = ..., deleted: bool = ...) -> None: ...

class PushNameSetting(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class PrimaryVersionAction(_message.Message):
    __slots__ = ["version"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str
    def __init__(self, version: _Optional[str] = ...) -> None: ...

class PrimaryFeature(_message.Message):
    __slots__ = ["flags"]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    flags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, flags: _Optional[_Iterable[str]] = ...) -> None: ...

class PnForLidChatAction(_message.Message):
    __slots__ = ["pnJid"]
    PNJID_FIELD_NUMBER: _ClassVar[int]
    pnJid: str
    def __init__(self, pnJid: _Optional[str] = ...) -> None: ...

class PinAction(_message.Message):
    __slots__ = ["pinned"]
    PINNED_FIELD_NUMBER: _ClassVar[int]
    pinned: bool
    def __init__(self, pinned: bool = ...) -> None: ...

class NuxAction(_message.Message):
    __slots__ = ["acknowledged"]
    ACKNOWLEDGED_FIELD_NUMBER: _ClassVar[int]
    acknowledged: bool
    def __init__(self, acknowledged: bool = ...) -> None: ...

class MuteAction(_message.Message):
    __slots__ = ["muted", "muteEndTimestamp", "autoMuted"]
    MUTED_FIELD_NUMBER: _ClassVar[int]
    MUTEENDTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    AUTOMUTED_FIELD_NUMBER: _ClassVar[int]
    muted: bool
    muteEndTimestamp: int
    autoMuted: bool
    def __init__(self, muted: bool = ..., muteEndTimestamp: _Optional[int] = ..., autoMuted: bool = ...) -> None: ...

class MarketingMessageBroadcastAction(_message.Message):
    __slots__ = ["repliedCount"]
    REPLIEDCOUNT_FIELD_NUMBER: _ClassVar[int]
    repliedCount: int
    def __init__(self, repliedCount: _Optional[int] = ...) -> None: ...

class MarketingMessageAction(_message.Message):
    __slots__ = ["name", "message", "msgType", "createdAt", "lastSentAt", "isDeleted"]
    class MarketingMessageMsgType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        TEXT: _ClassVar[MarketingMessageAction.MarketingMessageMsgType]
        IMAGE: _ClassVar[MarketingMessageAction.MarketingMessageMsgType]
        VIDEO: _ClassVar[MarketingMessageAction.MarketingMessageMsgType]
    TEXT: MarketingMessageAction.MarketingMessageMsgType
    IMAGE: MarketingMessageAction.MarketingMessageMsgType
    VIDEO: MarketingMessageAction.MarketingMessageMsgType
    NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MSGTYPE_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    LASTSENTAT_FIELD_NUMBER: _ClassVar[int]
    ISDELETED_FIELD_NUMBER: _ClassVar[int]
    name: str
    message: str
    msgType: MarketingMessageAction.MarketingMessageMsgType
    createdAt: int
    lastSentAt: int
    isDeleted: bool
    def __init__(self, name: _Optional[str] = ..., message: _Optional[str] = ..., msgType: _Optional[_Union[MarketingMessageAction.MarketingMessageMsgType, str]] = ..., createdAt: _Optional[int] = ..., lastSentAt: _Optional[int] = ..., isDeleted: bool = ...) -> None: ...

class MarkChatAsReadAction(_message.Message):
    __slots__ = ["read", "messageRange"]
    READ_FIELD_NUMBER: _ClassVar[int]
    MESSAGERANGE_FIELD_NUMBER: _ClassVar[int]
    read: bool
    messageRange: SyncActionMessageRange
    def __init__(self, read: bool = ..., messageRange: _Optional[_Union[SyncActionMessageRange, _Mapping]] = ...) -> None: ...

class LocaleSetting(_message.Message):
    __slots__ = ["locale"]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    locale: str
    def __init__(self, locale: _Optional[str] = ...) -> None: ...

class LabelEditAction(_message.Message):
    __slots__ = ["name", "color", "predefinedId", "deleted"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    PREDEFINEDID_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    name: str
    color: int
    predefinedId: int
    deleted: bool
    def __init__(self, name: _Optional[str] = ..., color: _Optional[int] = ..., predefinedId: _Optional[int] = ..., deleted: bool = ...) -> None: ...

class LabelAssociationAction(_message.Message):
    __slots__ = ["labeled"]
    LABELED_FIELD_NUMBER: _ClassVar[int]
    labeled: bool
    def __init__(self, labeled: bool = ...) -> None: ...

class KeyExpiration(_message.Message):
    __slots__ = ["expiredKeyEpoch"]
    EXPIREDKEYEPOCH_FIELD_NUMBER: _ClassVar[int]
    expiredKeyEpoch: int
    def __init__(self, expiredKeyEpoch: _Optional[int] = ...) -> None: ...

class ExternalWebBetaAction(_message.Message):
    __slots__ = ["isOptIn"]
    ISOPTIN_FIELD_NUMBER: _ClassVar[int]
    isOptIn: bool
    def __init__(self, isOptIn: bool = ...) -> None: ...

class DeleteMessageForMeAction(_message.Message):
    __slots__ = ["deleteMedia", "messageTimestamp"]
    DELETEMEDIA_FIELD_NUMBER: _ClassVar[int]
    MESSAGETIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    deleteMedia: bool
    messageTimestamp: int
    def __init__(self, deleteMedia: bool = ..., messageTimestamp: _Optional[int] = ...) -> None: ...

class DeleteChatAction(_message.Message):
    __slots__ = ["messageRange"]
    MESSAGERANGE_FIELD_NUMBER: _ClassVar[int]
    messageRange: SyncActionMessageRange
    def __init__(self, messageRange: _Optional[_Union[SyncActionMessageRange, _Mapping]] = ...) -> None: ...

class ContactAction(_message.Message):
    __slots__ = ["fullName", "firstName", "lidJid"]
    FULLNAME_FIELD_NUMBER: _ClassVar[int]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    LIDJID_FIELD_NUMBER: _ClassVar[int]
    fullName: str
    firstName: str
    lidJid: str
    def __init__(self, fullName: _Optional[str] = ..., firstName: _Optional[str] = ..., lidJid: _Optional[str] = ...) -> None: ...

class ClearChatAction(_message.Message):
    __slots__ = ["messageRange"]
    MESSAGERANGE_FIELD_NUMBER: _ClassVar[int]
    messageRange: SyncActionMessageRange
    def __init__(self, messageRange: _Optional[_Union[SyncActionMessageRange, _Mapping]] = ...) -> None: ...

class ChatAssignmentOpenedStatusAction(_message.Message):
    __slots__ = ["chatOpened"]
    CHATOPENED_FIELD_NUMBER: _ClassVar[int]
    chatOpened: bool
    def __init__(self, chatOpened: bool = ...) -> None: ...

class ChatAssignmentAction(_message.Message):
    __slots__ = ["deviceAgentID"]
    DEVICEAGENTID_FIELD_NUMBER: _ClassVar[int]
    deviceAgentID: str
    def __init__(self, deviceAgentID: _Optional[str] = ...) -> None: ...

class ArchiveChatAction(_message.Message):
    __slots__ = ["archived", "messageRange"]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    MESSAGERANGE_FIELD_NUMBER: _ClassVar[int]
    archived: bool
    messageRange: SyncActionMessageRange
    def __init__(self, archived: bool = ..., messageRange: _Optional[_Union[SyncActionMessageRange, _Mapping]] = ...) -> None: ...

class AndroidUnsupportedActions(_message.Message):
    __slots__ = ["allowed"]
    ALLOWED_FIELD_NUMBER: _ClassVar[int]
    allowed: bool
    def __init__(self, allowed: bool = ...) -> None: ...

class AgentAction(_message.Message):
    __slots__ = ["name", "deviceID", "isDeleted"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    ISDELETED_FIELD_NUMBER: _ClassVar[int]
    name: str
    deviceID: int
    isDeleted: bool
    def __init__(self, name: _Optional[str] = ..., deviceID: _Optional[int] = ..., isDeleted: bool = ...) -> None: ...

class SyncActionData(_message.Message):
    __slots__ = ["index", "value", "padding", "version"]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    PADDING_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    index: bytes
    value: SyncActionValue
    padding: bytes
    version: int
    def __init__(self, index: _Optional[bytes] = ..., value: _Optional[_Union[SyncActionValue, _Mapping]] = ..., padding: _Optional[bytes] = ..., version: _Optional[int] = ...) -> None: ...

class RecentEmojiWeight(_message.Message):
    __slots__ = ["emoji", "weight"]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    emoji: str
    weight: float
    def __init__(self, emoji: _Optional[str] = ..., weight: _Optional[float] = ...) -> None: ...

class VerifiedNameCertificate(_message.Message):
    __slots__ = ["details", "signature", "serverSignature"]
    class Details(_message.Message):
        __slots__ = ["serial", "issuer", "verifiedName", "localizedNames", "issueTime"]
        SERIAL_FIELD_NUMBER: _ClassVar[int]
        ISSUER_FIELD_NUMBER: _ClassVar[int]
        VERIFIEDNAME_FIELD_NUMBER: _ClassVar[int]
        LOCALIZEDNAMES_FIELD_NUMBER: _ClassVar[int]
        ISSUETIME_FIELD_NUMBER: _ClassVar[int]
        serial: int
        issuer: str
        verifiedName: str
        localizedNames: _containers.RepeatedCompositeFieldContainer[LocalizedName]
        issueTime: int
        def __init__(self, serial: _Optional[int] = ..., issuer: _Optional[str] = ..., verifiedName: _Optional[str] = ..., localizedNames: _Optional[_Iterable[_Union[LocalizedName, _Mapping]]] = ..., issueTime: _Optional[int] = ...) -> None: ...
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SERVERSIGNATURE_FIELD_NUMBER: _ClassVar[int]
    details: bytes
    signature: bytes
    serverSignature: bytes
    def __init__(self, details: _Optional[bytes] = ..., signature: _Optional[bytes] = ..., serverSignature: _Optional[bytes] = ...) -> None: ...

class LocalizedName(_message.Message):
    __slots__ = ["lg", "lc", "verifiedName"]
    LG_FIELD_NUMBER: _ClassVar[int]
    LC_FIELD_NUMBER: _ClassVar[int]
    VERIFIEDNAME_FIELD_NUMBER: _ClassVar[int]
    lg: str
    lc: str
    verifiedName: str
    def __init__(self, lg: _Optional[str] = ..., lc: _Optional[str] = ..., verifiedName: _Optional[str] = ...) -> None: ...

class BizIdentityInfo(_message.Message):
    __slots__ = ["vlevel", "vnameCert", "signed", "revoked", "hostStorage", "actualActors", "privacyModeTs", "featureControls"]
    class VerifiedLevelValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[BizIdentityInfo.VerifiedLevelValue]
        LOW: _ClassVar[BizIdentityInfo.VerifiedLevelValue]
        HIGH: _ClassVar[BizIdentityInfo.VerifiedLevelValue]
    UNKNOWN: BizIdentityInfo.VerifiedLevelValue
    LOW: BizIdentityInfo.VerifiedLevelValue
    HIGH: BizIdentityInfo.VerifiedLevelValue
    class HostStorageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        ON_PREMISE: _ClassVar[BizIdentityInfo.HostStorageType]
        FACEBOOK: _ClassVar[BizIdentityInfo.HostStorageType]
    ON_PREMISE: BizIdentityInfo.HostStorageType
    FACEBOOK: BizIdentityInfo.HostStorageType
    class ActualActorsType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        SELF: _ClassVar[BizIdentityInfo.ActualActorsType]
        BSP: _ClassVar[BizIdentityInfo.ActualActorsType]
    SELF: BizIdentityInfo.ActualActorsType
    BSP: BizIdentityInfo.ActualActorsType
    VLEVEL_FIELD_NUMBER: _ClassVar[int]
    VNAMECERT_FIELD_NUMBER: _ClassVar[int]
    SIGNED_FIELD_NUMBER: _ClassVar[int]
    REVOKED_FIELD_NUMBER: _ClassVar[int]
    HOSTSTORAGE_FIELD_NUMBER: _ClassVar[int]
    ACTUALACTORS_FIELD_NUMBER: _ClassVar[int]
    PRIVACYMODETS_FIELD_NUMBER: _ClassVar[int]
    FEATURECONTROLS_FIELD_NUMBER: _ClassVar[int]
    vlevel: BizIdentityInfo.VerifiedLevelValue
    vnameCert: VerifiedNameCertificate
    signed: bool
    revoked: bool
    hostStorage: BizIdentityInfo.HostStorageType
    actualActors: BizIdentityInfo.ActualActorsType
    privacyModeTs: int
    featureControls: int
    def __init__(self, vlevel: _Optional[_Union[BizIdentityInfo.VerifiedLevelValue, str]] = ..., vnameCert: _Optional[_Union[VerifiedNameCertificate, _Mapping]] = ..., signed: bool = ..., revoked: bool = ..., hostStorage: _Optional[_Union[BizIdentityInfo.HostStorageType, str]] = ..., actualActors: _Optional[_Union[BizIdentityInfo.ActualActorsType, str]] = ..., privacyModeTs: _Optional[int] = ..., featureControls: _Optional[int] = ...) -> None: ...

class BizAccountPayload(_message.Message):
    __slots__ = ["vnameCert", "bizAcctLinkInfo"]
    VNAMECERT_FIELD_NUMBER: _ClassVar[int]
    BIZACCTLINKINFO_FIELD_NUMBER: _ClassVar[int]
    vnameCert: VerifiedNameCertificate
    bizAcctLinkInfo: bytes
    def __init__(self, vnameCert: _Optional[_Union[VerifiedNameCertificate, _Mapping]] = ..., bizAcctLinkInfo: _Optional[bytes] = ...) -> None: ...

class BizAccountLinkInfo(_message.Message):
    __slots__ = ["whatsappBizAcctFbid", "whatsappAcctNumber", "issueTime", "hostStorage", "accountType"]
    class HostStorageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        ON_PREMISE: _ClassVar[BizAccountLinkInfo.HostStorageType]
        FACEBOOK: _ClassVar[BizAccountLinkInfo.HostStorageType]
    ON_PREMISE: BizAccountLinkInfo.HostStorageType
    FACEBOOK: BizAccountLinkInfo.HostStorageType
    class AccountType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        ENTERPRISE: _ClassVar[BizAccountLinkInfo.AccountType]
    ENTERPRISE: BizAccountLinkInfo.AccountType
    WHATSAPPBIZACCTFBID_FIELD_NUMBER: _ClassVar[int]
    WHATSAPPACCTNUMBER_FIELD_NUMBER: _ClassVar[int]
    ISSUETIME_FIELD_NUMBER: _ClassVar[int]
    HOSTSTORAGE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTTYPE_FIELD_NUMBER: _ClassVar[int]
    whatsappBizAcctFbid: int
    whatsappAcctNumber: str
    issueTime: int
    hostStorage: BizAccountLinkInfo.HostStorageType
    accountType: BizAccountLinkInfo.AccountType
    def __init__(self, whatsappBizAcctFbid: _Optional[int] = ..., whatsappAcctNumber: _Optional[str] = ..., issueTime: _Optional[int] = ..., hostStorage: _Optional[_Union[BizAccountLinkInfo.HostStorageType, str]] = ..., accountType: _Optional[_Union[BizAccountLinkInfo.AccountType, str]] = ...) -> None: ...

class HandshakeMessage(_message.Message):
    __slots__ = ["clientHello", "serverHello", "clientFinish"]
    CLIENTHELLO_FIELD_NUMBER: _ClassVar[int]
    SERVERHELLO_FIELD_NUMBER: _ClassVar[int]
    CLIENTFINISH_FIELD_NUMBER: _ClassVar[int]
    clientHello: HandshakeClientHello
    serverHello: HandshakeServerHello
    clientFinish: HandshakeClientFinish
    def __init__(self, clientHello: _Optional[_Union[HandshakeClientHello, _Mapping]] = ..., serverHello: _Optional[_Union[HandshakeServerHello, _Mapping]] = ..., clientFinish: _Optional[_Union[HandshakeClientFinish, _Mapping]] = ...) -> None: ...

class HandshakeServerHello(_message.Message):
    __slots__ = ["ephemeral", "static", "payload"]
    EPHEMERAL_FIELD_NUMBER: _ClassVar[int]
    STATIC_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ephemeral: bytes
    static: bytes
    payload: bytes
    def __init__(self, ephemeral: _Optional[bytes] = ..., static: _Optional[bytes] = ..., payload: _Optional[bytes] = ...) -> None: ...

class HandshakeClientHello(_message.Message):
    __slots__ = ["ephemeral", "static", "payload"]
    EPHEMERAL_FIELD_NUMBER: _ClassVar[int]
    STATIC_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ephemeral: bytes
    static: bytes
    payload: bytes
    def __init__(self, ephemeral: _Optional[bytes] = ..., static: _Optional[bytes] = ..., payload: _Optional[bytes] = ...) -> None: ...

class HandshakeClientFinish(_message.Message):
    __slots__ = ["static", "payload"]
    STATIC_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    static: bytes
    payload: bytes
    def __init__(self, static: _Optional[bytes] = ..., payload: _Optional[bytes] = ...) -> None: ...

class ClientPayload(_message.Message):
    __slots__ = ["username", "passive", "userAgent", "webInfo", "pushName", "sessionId", "shortConnect", "connectType", "connectReason", "shards", "dnsSource", "connectAttemptCount", "device", "devicePairingData", "product", "fbCat", "fbUserAgent", "oc", "lc", "iosAppExtension", "fbAppId", "fbDeviceId", "pull", "paddingBytes", "yearClass", "memClass", "interopData"]
    class Product(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        WHATSAPP: _ClassVar[ClientPayload.Product]
        MESSENGER: _ClassVar[ClientPayload.Product]
        INTEROP: _ClassVar[ClientPayload.Product]
    WHATSAPP: ClientPayload.Product
    MESSENGER: ClientPayload.Product
    INTEROP: ClientPayload.Product
    class IOSAppExtension(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        SHARE_EXTENSION: _ClassVar[ClientPayload.IOSAppExtension]
        SERVICE_EXTENSION: _ClassVar[ClientPayload.IOSAppExtension]
        INTENTS_EXTENSION: _ClassVar[ClientPayload.IOSAppExtension]
    SHARE_EXTENSION: ClientPayload.IOSAppExtension
    SERVICE_EXTENSION: ClientPayload.IOSAppExtension
    INTENTS_EXTENSION: ClientPayload.IOSAppExtension
    class ConnectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        CELLULAR_UNKNOWN: _ClassVar[ClientPayload.ConnectType]
        WIFI_UNKNOWN: _ClassVar[ClientPayload.ConnectType]
        CELLULAR_EDGE: _ClassVar[ClientPayload.ConnectType]
        CELLULAR_IDEN: _ClassVar[ClientPayload.ConnectType]
        CELLULAR_UMTS: _ClassVar[ClientPayload.ConnectType]
        CELLULAR_EVDO: _ClassVar[ClientPayload.ConnectType]
        CELLULAR_GPRS: _ClassVar[ClientPayload.ConnectType]
        CELLULAR_HSDPA: _ClassVar[ClientPayload.ConnectType]
        CELLULAR_HSUPA: _ClassVar[ClientPayload.ConnectType]
        CELLULAR_HSPA: _ClassVar[ClientPayload.ConnectType]
        CELLULAR_CDMA: _ClassVar[ClientPayload.ConnectType]
        CELLULAR_1XRTT: _ClassVar[ClientPayload.ConnectType]
        CELLULAR_EHRPD: _ClassVar[ClientPayload.ConnectType]
        CELLULAR_LTE: _ClassVar[ClientPayload.ConnectType]
        CELLULAR_HSPAP: _ClassVar[ClientPayload.ConnectType]
    CELLULAR_UNKNOWN: ClientPayload.ConnectType
    WIFI_UNKNOWN: ClientPayload.ConnectType
    CELLULAR_EDGE: ClientPayload.ConnectType
    CELLULAR_IDEN: ClientPayload.ConnectType
    CELLULAR_UMTS: ClientPayload.ConnectType
    CELLULAR_EVDO: ClientPayload.ConnectType
    CELLULAR_GPRS: ClientPayload.ConnectType
    CELLULAR_HSDPA: ClientPayload.ConnectType
    CELLULAR_HSUPA: ClientPayload.ConnectType
    CELLULAR_HSPA: ClientPayload.ConnectType
    CELLULAR_CDMA: ClientPayload.ConnectType
    CELLULAR_1XRTT: ClientPayload.ConnectType
    CELLULAR_EHRPD: ClientPayload.ConnectType
    CELLULAR_LTE: ClientPayload.ConnectType
    CELLULAR_HSPAP: ClientPayload.ConnectType
    class ConnectReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        PUSH: _ClassVar[ClientPayload.ConnectReason]
        USER_ACTIVATED: _ClassVar[ClientPayload.ConnectReason]
        SCHEDULED: _ClassVar[ClientPayload.ConnectReason]
        ERROR_RECONNECT: _ClassVar[ClientPayload.ConnectReason]
        NETWORK_SWITCH: _ClassVar[ClientPayload.ConnectReason]
        PING_RECONNECT: _ClassVar[ClientPayload.ConnectReason]
        UNKNOWN: _ClassVar[ClientPayload.ConnectReason]
    PUSH: ClientPayload.ConnectReason
    USER_ACTIVATED: ClientPayload.ConnectReason
    SCHEDULED: ClientPayload.ConnectReason
    ERROR_RECONNECT: ClientPayload.ConnectReason
    NETWORK_SWITCH: ClientPayload.ConnectReason
    PING_RECONNECT: ClientPayload.ConnectReason
    UNKNOWN: ClientPayload.ConnectReason
    class WebInfo(_message.Message):
        __slots__ = ["refToken", "version", "webdPayload", "webSubPlatform"]
        class WebSubPlatform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            WEB_BROWSER: _ClassVar[ClientPayload.WebInfo.WebSubPlatform]
            APP_STORE: _ClassVar[ClientPayload.WebInfo.WebSubPlatform]
            WIN_STORE: _ClassVar[ClientPayload.WebInfo.WebSubPlatform]
            DARWIN: _ClassVar[ClientPayload.WebInfo.WebSubPlatform]
            WIN32: _ClassVar[ClientPayload.WebInfo.WebSubPlatform]
        WEB_BROWSER: ClientPayload.WebInfo.WebSubPlatform
        APP_STORE: ClientPayload.WebInfo.WebSubPlatform
        WIN_STORE: ClientPayload.WebInfo.WebSubPlatform
        DARWIN: ClientPayload.WebInfo.WebSubPlatform
        WIN32: ClientPayload.WebInfo.WebSubPlatform
        class WebdPayload(_message.Message):
            __slots__ = ["usesParticipantInKey", "supportsStarredMessages", "supportsDocumentMessages", "supportsUrlMessages", "supportsMediaRetry", "supportsE2EImage", "supportsE2EVideo", "supportsE2EAudio", "supportsE2EDocument", "documentTypes", "features"]
            USESPARTICIPANTINKEY_FIELD_NUMBER: _ClassVar[int]
            SUPPORTSSTARREDMESSAGES_FIELD_NUMBER: _ClassVar[int]
            SUPPORTSDOCUMENTMESSAGES_FIELD_NUMBER: _ClassVar[int]
            SUPPORTSURLMESSAGES_FIELD_NUMBER: _ClassVar[int]
            SUPPORTSMEDIARETRY_FIELD_NUMBER: _ClassVar[int]
            SUPPORTSE2EIMAGE_FIELD_NUMBER: _ClassVar[int]
            SUPPORTSE2EVIDEO_FIELD_NUMBER: _ClassVar[int]
            SUPPORTSE2EAUDIO_FIELD_NUMBER: _ClassVar[int]
            SUPPORTSE2EDOCUMENT_FIELD_NUMBER: _ClassVar[int]
            DOCUMENTTYPES_FIELD_NUMBER: _ClassVar[int]
            FEATURES_FIELD_NUMBER: _ClassVar[int]
            usesParticipantInKey: bool
            supportsStarredMessages: bool
            supportsDocumentMessages: bool
            supportsUrlMessages: bool
            supportsMediaRetry: bool
            supportsE2EImage: bool
            supportsE2EVideo: bool
            supportsE2EAudio: bool
            supportsE2EDocument: bool
            documentTypes: str
            features: bytes
            def __init__(self, usesParticipantInKey: bool = ..., supportsStarredMessages: bool = ..., supportsDocumentMessages: bool = ..., supportsUrlMessages: bool = ..., supportsMediaRetry: bool = ..., supportsE2EImage: bool = ..., supportsE2EVideo: bool = ..., supportsE2EAudio: bool = ..., supportsE2EDocument: bool = ..., documentTypes: _Optional[str] = ..., features: _Optional[bytes] = ...) -> None: ...
        REFTOKEN_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        WEBDPAYLOAD_FIELD_NUMBER: _ClassVar[int]
        WEBSUBPLATFORM_FIELD_NUMBER: _ClassVar[int]
        refToken: str
        version: str
        webdPayload: ClientPayload.WebInfo.WebdPayload
        webSubPlatform: ClientPayload.WebInfo.WebSubPlatform
        def __init__(self, refToken: _Optional[str] = ..., version: _Optional[str] = ..., webdPayload: _Optional[_Union[ClientPayload.WebInfo.WebdPayload, _Mapping]] = ..., webSubPlatform: _Optional[_Union[ClientPayload.WebInfo.WebSubPlatform, str]] = ...) -> None: ...
    class UserAgent(_message.Message):
        __slots__ = ["platform", "appVersion", "mcc", "mnc", "osVersion", "manufacturer", "device", "osBuildNumber", "phoneId", "releaseChannel", "localeLanguageIso6391", "localeCountryIso31661Alpha2", "deviceBoard"]
        class ReleaseChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            RELEASE: _ClassVar[ClientPayload.UserAgent.ReleaseChannel]
            BETA: _ClassVar[ClientPayload.UserAgent.ReleaseChannel]
            ALPHA: _ClassVar[ClientPayload.UserAgent.ReleaseChannel]
            DEBUG: _ClassVar[ClientPayload.UserAgent.ReleaseChannel]
        RELEASE: ClientPayload.UserAgent.ReleaseChannel
        BETA: ClientPayload.UserAgent.ReleaseChannel
        ALPHA: ClientPayload.UserAgent.ReleaseChannel
        DEBUG: ClientPayload.UserAgent.ReleaseChannel
        class Platform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            ANDROID: _ClassVar[ClientPayload.UserAgent.Platform]
            IOS: _ClassVar[ClientPayload.UserAgent.Platform]
            WINDOWS_PHONE: _ClassVar[ClientPayload.UserAgent.Platform]
            BLACKBERRY: _ClassVar[ClientPayload.UserAgent.Platform]
            BLACKBERRYX: _ClassVar[ClientPayload.UserAgent.Platform]
            S40: _ClassVar[ClientPayload.UserAgent.Platform]
            S60: _ClassVar[ClientPayload.UserAgent.Platform]
            PYTHON_CLIENT: _ClassVar[ClientPayload.UserAgent.Platform]
            TIZEN: _ClassVar[ClientPayload.UserAgent.Platform]
            ENTERPRISE: _ClassVar[ClientPayload.UserAgent.Platform]
            SMB_ANDROID: _ClassVar[ClientPayload.UserAgent.Platform]
            KAIOS: _ClassVar[ClientPayload.UserAgent.Platform]
            SMB_IOS: _ClassVar[ClientPayload.UserAgent.Platform]
            WINDOWS: _ClassVar[ClientPayload.UserAgent.Platform]
            WEB: _ClassVar[ClientPayload.UserAgent.Platform]
            PORTAL: _ClassVar[ClientPayload.UserAgent.Platform]
            GREEN_ANDROID: _ClassVar[ClientPayload.UserAgent.Platform]
            GREEN_IPHONE: _ClassVar[ClientPayload.UserAgent.Platform]
            BLUE_ANDROID: _ClassVar[ClientPayload.UserAgent.Platform]
            BLUE_IPHONE: _ClassVar[ClientPayload.UserAgent.Platform]
            FBLITE_ANDROID: _ClassVar[ClientPayload.UserAgent.Platform]
            MLITE_ANDROID: _ClassVar[ClientPayload.UserAgent.Platform]
            IGLITE_ANDROID: _ClassVar[ClientPayload.UserAgent.Platform]
            PAGE: _ClassVar[ClientPayload.UserAgent.Platform]
            MACOS: _ClassVar[ClientPayload.UserAgent.Platform]
            OCULUS_MSG: _ClassVar[ClientPayload.UserAgent.Platform]
            OCULUS_CALL: _ClassVar[ClientPayload.UserAgent.Platform]
            MILAN: _ClassVar[ClientPayload.UserAgent.Platform]
            CAPI: _ClassVar[ClientPayload.UserAgent.Platform]
            WEAROS: _ClassVar[ClientPayload.UserAgent.Platform]
            ARDEVICE: _ClassVar[ClientPayload.UserAgent.Platform]
            VRDEVICE: _ClassVar[ClientPayload.UserAgent.Platform]
            BLUE_WEB: _ClassVar[ClientPayload.UserAgent.Platform]
            IPAD: _ClassVar[ClientPayload.UserAgent.Platform]
        ANDROID: ClientPayload.UserAgent.Platform
        IOS: ClientPayload.UserAgent.Platform
        WINDOWS_PHONE: ClientPayload.UserAgent.Platform
        BLACKBERRY: ClientPayload.UserAgent.Platform
        BLACKBERRYX: ClientPayload.UserAgent.Platform
        S40: ClientPayload.UserAgent.Platform
        S60: ClientPayload.UserAgent.Platform
        PYTHON_CLIENT: ClientPayload.UserAgent.Platform
        TIZEN: ClientPayload.UserAgent.Platform
        ENTERPRISE: ClientPayload.UserAgent.Platform
        SMB_ANDROID: ClientPayload.UserAgent.Platform
        KAIOS: ClientPayload.UserAgent.Platform
        SMB_IOS: ClientPayload.UserAgent.Platform
        WINDOWS: ClientPayload.UserAgent.Platform
        WEB: ClientPayload.UserAgent.Platform
        PORTAL: ClientPayload.UserAgent.Platform
        GREEN_ANDROID: ClientPayload.UserAgent.Platform
        GREEN_IPHONE: ClientPayload.UserAgent.Platform
        BLUE_ANDROID: ClientPayload.UserAgent.Platform
        BLUE_IPHONE: ClientPayload.UserAgent.Platform
        FBLITE_ANDROID: ClientPayload.UserAgent.Platform
        MLITE_ANDROID: ClientPayload.UserAgent.Platform
        IGLITE_ANDROID: ClientPayload.UserAgent.Platform
        PAGE: ClientPayload.UserAgent.Platform
        MACOS: ClientPayload.UserAgent.Platform
        OCULUS_MSG: ClientPayload.UserAgent.Platform
        OCULUS_CALL: ClientPayload.UserAgent.Platform
        MILAN: ClientPayload.UserAgent.Platform
        CAPI: ClientPayload.UserAgent.Platform
        WEAROS: ClientPayload.UserAgent.Platform
        ARDEVICE: ClientPayload.UserAgent.Platform
        VRDEVICE: ClientPayload.UserAgent.Platform
        BLUE_WEB: ClientPayload.UserAgent.Platform
        IPAD: ClientPayload.UserAgent.Platform
        class AppVersion(_message.Message):
            __slots__ = ["primary", "secondary", "tertiary", "quaternary", "quinary"]
            PRIMARY_FIELD_NUMBER: _ClassVar[int]
            SECONDARY_FIELD_NUMBER: _ClassVar[int]
            TERTIARY_FIELD_NUMBER: _ClassVar[int]
            QUATERNARY_FIELD_NUMBER: _ClassVar[int]
            QUINARY_FIELD_NUMBER: _ClassVar[int]
            primary: int
            secondary: int
            tertiary: int
            quaternary: int
            quinary: int
            def __init__(self, primary: _Optional[int] = ..., secondary: _Optional[int] = ..., tertiary: _Optional[int] = ..., quaternary: _Optional[int] = ..., quinary: _Optional[int] = ...) -> None: ...
        PLATFORM_FIELD_NUMBER: _ClassVar[int]
        APPVERSION_FIELD_NUMBER: _ClassVar[int]
        MCC_FIELD_NUMBER: _ClassVar[int]
        MNC_FIELD_NUMBER: _ClassVar[int]
        OSVERSION_FIELD_NUMBER: _ClassVar[int]
        MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
        DEVICE_FIELD_NUMBER: _ClassVar[int]
        OSBUILDNUMBER_FIELD_NUMBER: _ClassVar[int]
        PHONEID_FIELD_NUMBER: _ClassVar[int]
        RELEASECHANNEL_FIELD_NUMBER: _ClassVar[int]
        LOCALELANGUAGEISO6391_FIELD_NUMBER: _ClassVar[int]
        LOCALECOUNTRYISO31661ALPHA2_FIELD_NUMBER: _ClassVar[int]
        DEVICEBOARD_FIELD_NUMBER: _ClassVar[int]
        platform: ClientPayload.UserAgent.Platform
        appVersion: ClientPayload.UserAgent.AppVersion
        mcc: str
        mnc: str
        osVersion: str
        manufacturer: str
        device: str
        osBuildNumber: str
        phoneId: str
        releaseChannel: ClientPayload.UserAgent.ReleaseChannel
        localeLanguageIso6391: str
        localeCountryIso31661Alpha2: str
        deviceBoard: str
        def __init__(self, platform: _Optional[_Union[ClientPayload.UserAgent.Platform, str]] = ..., appVersion: _Optional[_Union[ClientPayload.UserAgent.AppVersion, _Mapping]] = ..., mcc: _Optional[str] = ..., mnc: _Optional[str] = ..., osVersion: _Optional[str] = ..., manufacturer: _Optional[str] = ..., device: _Optional[str] = ..., osBuildNumber: _Optional[str] = ..., phoneId: _Optional[str] = ..., releaseChannel: _Optional[_Union[ClientPayload.UserAgent.ReleaseChannel, str]] = ..., localeLanguageIso6391: _Optional[str] = ..., localeCountryIso31661Alpha2: _Optional[str] = ..., deviceBoard: _Optional[str] = ...) -> None: ...
    class InteropData(_message.Message):
        __slots__ = ["accountId", "integratorId", "token"]
        ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        INTEGRATORID_FIELD_NUMBER: _ClassVar[int]
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        accountId: int
        integratorId: int
        token: bytes
        def __init__(self, accountId: _Optional[int] = ..., integratorId: _Optional[int] = ..., token: _Optional[bytes] = ...) -> None: ...
    class DevicePairingRegistrationData(_message.Message):
        __slots__ = ["eRegid", "eKeytype", "eIdent", "eSkeyId", "eSkeyVal", "eSkeySig", "buildHash", "deviceProps"]
        EREGID_FIELD_NUMBER: _ClassVar[int]
        EKEYTYPE_FIELD_NUMBER: _ClassVar[int]
        EIDENT_FIELD_NUMBER: _ClassVar[int]
        ESKEYID_FIELD_NUMBER: _ClassVar[int]
        ESKEYVAL_FIELD_NUMBER: _ClassVar[int]
        ESKEYSIG_FIELD_NUMBER: _ClassVar[int]
        BUILDHASH_FIELD_NUMBER: _ClassVar[int]
        DEVICEPROPS_FIELD_NUMBER: _ClassVar[int]
        eRegid: bytes
        eKeytype: bytes
        eIdent: bytes
        eSkeyId: bytes
        eSkeyVal: bytes
        eSkeySig: bytes
        buildHash: bytes
        deviceProps: bytes
        def __init__(self, eRegid: _Optional[bytes] = ..., eKeytype: _Optional[bytes] = ..., eIdent: _Optional[bytes] = ..., eSkeyId: _Optional[bytes] = ..., eSkeyVal: _Optional[bytes] = ..., eSkeySig: _Optional[bytes] = ..., buildHash: _Optional[bytes] = ..., deviceProps: _Optional[bytes] = ...) -> None: ...
    class DNSSource(_message.Message):
        __slots__ = ["dnsMethod", "appCached"]
        class DNSResolutionMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            SYSTEM: _ClassVar[ClientPayload.DNSSource.DNSResolutionMethod]
            GOOGLE: _ClassVar[ClientPayload.DNSSource.DNSResolutionMethod]
            HARDCODED: _ClassVar[ClientPayload.DNSSource.DNSResolutionMethod]
            OVERRIDE: _ClassVar[ClientPayload.DNSSource.DNSResolutionMethod]
            FALLBACK: _ClassVar[ClientPayload.DNSSource.DNSResolutionMethod]
        SYSTEM: ClientPayload.DNSSource.DNSResolutionMethod
        GOOGLE: ClientPayload.DNSSource.DNSResolutionMethod
        HARDCODED: ClientPayload.DNSSource.DNSResolutionMethod
        OVERRIDE: ClientPayload.DNSSource.DNSResolutionMethod
        FALLBACK: ClientPayload.DNSSource.DNSResolutionMethod
        DNSMETHOD_FIELD_NUMBER: _ClassVar[int]
        APPCACHED_FIELD_NUMBER: _ClassVar[int]
        dnsMethod: ClientPayload.DNSSource.DNSResolutionMethod
        appCached: bool
        def __init__(self, dnsMethod: _Optional[_Union[ClientPayload.DNSSource.DNSResolutionMethod, str]] = ..., appCached: bool = ...) -> None: ...
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSIVE_FIELD_NUMBER: _ClassVar[int]
    USERAGENT_FIELD_NUMBER: _ClassVar[int]
    WEBINFO_FIELD_NUMBER: _ClassVar[int]
    PUSHNAME_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    SHORTCONNECT_FIELD_NUMBER: _ClassVar[int]
    CONNECTTYPE_FIELD_NUMBER: _ClassVar[int]
    CONNECTREASON_FIELD_NUMBER: _ClassVar[int]
    SHARDS_FIELD_NUMBER: _ClassVar[int]
    DNSSOURCE_FIELD_NUMBER: _ClassVar[int]
    CONNECTATTEMPTCOUNT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    DEVICEPAIRINGDATA_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    FBCAT_FIELD_NUMBER: _ClassVar[int]
    FBUSERAGENT_FIELD_NUMBER: _ClassVar[int]
    OC_FIELD_NUMBER: _ClassVar[int]
    LC_FIELD_NUMBER: _ClassVar[int]
    IOSAPPEXTENSION_FIELD_NUMBER: _ClassVar[int]
    FBAPPID_FIELD_NUMBER: _ClassVar[int]
    FBDEVICEID_FIELD_NUMBER: _ClassVar[int]
    PULL_FIELD_NUMBER: _ClassVar[int]
    PADDINGBYTES_FIELD_NUMBER: _ClassVar[int]
    YEARCLASS_FIELD_NUMBER: _ClassVar[int]
    MEMCLASS_FIELD_NUMBER: _ClassVar[int]
    INTEROPDATA_FIELD_NUMBER: _ClassVar[int]
    username: int
    passive: bool
    userAgent: ClientPayload.UserAgent
    webInfo: ClientPayload.WebInfo
    pushName: str
    sessionId: int
    shortConnect: bool
    connectType: ClientPayload.ConnectType
    connectReason: ClientPayload.ConnectReason
    shards: _containers.RepeatedScalarFieldContainer[int]
    dnsSource: ClientPayload.DNSSource
    connectAttemptCount: int
    device: int
    devicePairingData: ClientPayload.DevicePairingRegistrationData
    product: ClientPayload.Product
    fbCat: bytes
    fbUserAgent: bytes
    oc: bool
    lc: int
    iosAppExtension: ClientPayload.IOSAppExtension
    fbAppId: int
    fbDeviceId: bytes
    pull: bool
    paddingBytes: bytes
    yearClass: int
    memClass: int
    interopData: ClientPayload.InteropData
    def __init__(self, username: _Optional[int] = ..., passive: bool = ..., userAgent: _Optional[_Union[ClientPayload.UserAgent, _Mapping]] = ..., webInfo: _Optional[_Union[ClientPayload.WebInfo, _Mapping]] = ..., pushName: _Optional[str] = ..., sessionId: _Optional[int] = ..., shortConnect: bool = ..., connectType: _Optional[_Union[ClientPayload.ConnectType, str]] = ..., connectReason: _Optional[_Union[ClientPayload.ConnectReason, str]] = ..., shards: _Optional[_Iterable[int]] = ..., dnsSource: _Optional[_Union[ClientPayload.DNSSource, _Mapping]] = ..., connectAttemptCount: _Optional[int] = ..., device: _Optional[int] = ..., devicePairingData: _Optional[_Union[ClientPayload.DevicePairingRegistrationData, _Mapping]] = ..., product: _Optional[_Union[ClientPayload.Product, str]] = ..., fbCat: _Optional[bytes] = ..., fbUserAgent: _Optional[bytes] = ..., oc: bool = ..., lc: _Optional[int] = ..., iosAppExtension: _Optional[_Union[ClientPayload.IOSAppExtension, str]] = ..., fbAppId: _Optional[int] = ..., fbDeviceId: _Optional[bytes] = ..., pull: bool = ..., paddingBytes: _Optional[bytes] = ..., yearClass: _Optional[int] = ..., memClass: _Optional[int] = ..., interopData: _Optional[_Union[ClientPayload.InteropData, _Mapping]] = ...) -> None: ...

class WebNotificationsInfo(_message.Message):
    __slots__ = ["timestamp", "unreadChats", "notifyMessageCount", "notifyMessages"]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UNREADCHATS_FIELD_NUMBER: _ClassVar[int]
    NOTIFYMESSAGECOUNT_FIELD_NUMBER: _ClassVar[int]
    NOTIFYMESSAGES_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    unreadChats: int
    notifyMessageCount: int
    notifyMessages: _containers.RepeatedCompositeFieldContainer[WebMessageInfo]
    def __init__(self, timestamp: _Optional[int] = ..., unreadChats: _Optional[int] = ..., notifyMessageCount: _Optional[int] = ..., notifyMessages: _Optional[_Iterable[_Union[WebMessageInfo, _Mapping]]] = ...) -> None: ...

class WebMessageInfo(_message.Message):
    __slots__ = ["key", "message", "messageTimestamp", "status", "participant", "messageC2STimestamp", "ignore", "starred", "broadcast", "pushName", "mediaCiphertextSha256", "multicast", "urlText", "urlNumber", "messageStubType", "clearMedia", "messageStubParameters", "duration", "labels", "paymentInfo", "finalLiveLocation", "quotedPaymentInfo", "ephemeralStartTimestamp", "ephemeralDuration", "ephemeralOffToOn", "ephemeralOutOfSync", "bizPrivacyStatus", "verifiedBizName", "mediaData", "photoChange", "userReceipt", "reactions", "quotedStickerData", "futureproofData", "statusPsa", "pollUpdates", "pollAdditionalMetadata", "agentId", "statusAlreadyViewed", "messageSecret", "keepInChat", "originalSelfAuthorUserJidString", "revokeMessageTimestamp"]
    class StubType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[WebMessageInfo.StubType]
        REVOKE: _ClassVar[WebMessageInfo.StubType]
        CIPHERTEXT: _ClassVar[WebMessageInfo.StubType]
        FUTUREPROOF: _ClassVar[WebMessageInfo.StubType]
        NON_VERIFIED_TRANSITION: _ClassVar[WebMessageInfo.StubType]
        UNVERIFIED_TRANSITION: _ClassVar[WebMessageInfo.StubType]
        VERIFIED_TRANSITION: _ClassVar[WebMessageInfo.StubType]
        VERIFIED_LOW_UNKNOWN: _ClassVar[WebMessageInfo.StubType]
        VERIFIED_HIGH: _ClassVar[WebMessageInfo.StubType]
        VERIFIED_INITIAL_UNKNOWN: _ClassVar[WebMessageInfo.StubType]
        VERIFIED_INITIAL_LOW: _ClassVar[WebMessageInfo.StubType]
        VERIFIED_INITIAL_HIGH: _ClassVar[WebMessageInfo.StubType]
        VERIFIED_TRANSITION_ANY_TO_NONE: _ClassVar[WebMessageInfo.StubType]
        VERIFIED_TRANSITION_ANY_TO_HIGH: _ClassVar[WebMessageInfo.StubType]
        VERIFIED_TRANSITION_HIGH_TO_LOW: _ClassVar[WebMessageInfo.StubType]
        VERIFIED_TRANSITION_HIGH_TO_UNKNOWN: _ClassVar[WebMessageInfo.StubType]
        VERIFIED_TRANSITION_UNKNOWN_TO_LOW: _ClassVar[WebMessageInfo.StubType]
        VERIFIED_TRANSITION_LOW_TO_UNKNOWN: _ClassVar[WebMessageInfo.StubType]
        VERIFIED_TRANSITION_NONE_TO_LOW: _ClassVar[WebMessageInfo.StubType]
        VERIFIED_TRANSITION_NONE_TO_UNKNOWN: _ClassVar[WebMessageInfo.StubType]
        GROUP_CREATE: _ClassVar[WebMessageInfo.StubType]
        GROUP_CHANGE_SUBJECT: _ClassVar[WebMessageInfo.StubType]
        GROUP_CHANGE_ICON: _ClassVar[WebMessageInfo.StubType]
        GROUP_CHANGE_INVITE_LINK: _ClassVar[WebMessageInfo.StubType]
        GROUP_CHANGE_DESCRIPTION: _ClassVar[WebMessageInfo.StubType]
        GROUP_CHANGE_RESTRICT: _ClassVar[WebMessageInfo.StubType]
        GROUP_CHANGE_ANNOUNCE: _ClassVar[WebMessageInfo.StubType]
        GROUP_PARTICIPANT_ADD: _ClassVar[WebMessageInfo.StubType]
        GROUP_PARTICIPANT_REMOVE: _ClassVar[WebMessageInfo.StubType]
        GROUP_PARTICIPANT_PROMOTE: _ClassVar[WebMessageInfo.StubType]
        GROUP_PARTICIPANT_DEMOTE: _ClassVar[WebMessageInfo.StubType]
        GROUP_PARTICIPANT_INVITE: _ClassVar[WebMessageInfo.StubType]
        GROUP_PARTICIPANT_LEAVE: _ClassVar[WebMessageInfo.StubType]
        GROUP_PARTICIPANT_CHANGE_NUMBER: _ClassVar[WebMessageInfo.StubType]
        BROADCAST_CREATE: _ClassVar[WebMessageInfo.StubType]
        BROADCAST_ADD: _ClassVar[WebMessageInfo.StubType]
        BROADCAST_REMOVE: _ClassVar[WebMessageInfo.StubType]
        GENERIC_NOTIFICATION: _ClassVar[WebMessageInfo.StubType]
        E2E_IDENTITY_CHANGED: _ClassVar[WebMessageInfo.StubType]
        E2E_ENCRYPTED: _ClassVar[WebMessageInfo.StubType]
        CALL_MISSED_VOICE: _ClassVar[WebMessageInfo.StubType]
        CALL_MISSED_VIDEO: _ClassVar[WebMessageInfo.StubType]
        INDIVIDUAL_CHANGE_NUMBER: _ClassVar[WebMessageInfo.StubType]
        GROUP_DELETE: _ClassVar[WebMessageInfo.StubType]
        GROUP_ANNOUNCE_MODE_MESSAGE_BOUNCE: _ClassVar[WebMessageInfo.StubType]
        CALL_MISSED_GROUP_VOICE: _ClassVar[WebMessageInfo.StubType]
        CALL_MISSED_GROUP_VIDEO: _ClassVar[WebMessageInfo.StubType]
        PAYMENT_CIPHERTEXT: _ClassVar[WebMessageInfo.StubType]
        PAYMENT_FUTUREPROOF: _ClassVar[WebMessageInfo.StubType]
        PAYMENT_TRANSACTION_STATUS_UPDATE_FAILED: _ClassVar[WebMessageInfo.StubType]
        PAYMENT_TRANSACTION_STATUS_UPDATE_REFUNDED: _ClassVar[WebMessageInfo.StubType]
        PAYMENT_TRANSACTION_STATUS_UPDATE_REFUND_FAILED: _ClassVar[WebMessageInfo.StubType]
        PAYMENT_TRANSACTION_STATUS_RECEIVER_PENDING_SETUP: _ClassVar[WebMessageInfo.StubType]
        PAYMENT_TRANSACTION_STATUS_RECEIVER_SUCCESS_AFTER_HICCUP: _ClassVar[WebMessageInfo.StubType]
        PAYMENT_ACTION_ACCOUNT_SETUP_REMINDER: _ClassVar[WebMessageInfo.StubType]
        PAYMENT_ACTION_SEND_PAYMENT_REMINDER: _ClassVar[WebMessageInfo.StubType]
        PAYMENT_ACTION_SEND_PAYMENT_INVITATION: _ClassVar[WebMessageInfo.StubType]
        PAYMENT_ACTION_REQUEST_DECLINED: _ClassVar[WebMessageInfo.StubType]
        PAYMENT_ACTION_REQUEST_EXPIRED: _ClassVar[WebMessageInfo.StubType]
        PAYMENT_ACTION_REQUEST_CANCELLED: _ClassVar[WebMessageInfo.StubType]
        BIZ_VERIFIED_TRANSITION_TOP_TO_BOTTOM: _ClassVar[WebMessageInfo.StubType]
        BIZ_VERIFIED_TRANSITION_BOTTOM_TO_TOP: _ClassVar[WebMessageInfo.StubType]
        BIZ_INTRO_TOP: _ClassVar[WebMessageInfo.StubType]
        BIZ_INTRO_BOTTOM: _ClassVar[WebMessageInfo.StubType]
        BIZ_NAME_CHANGE: _ClassVar[WebMessageInfo.StubType]
        BIZ_MOVE_TO_CONSUMER_APP: _ClassVar[WebMessageInfo.StubType]
        BIZ_TWO_TIER_MIGRATION_TOP: _ClassVar[WebMessageInfo.StubType]
        BIZ_TWO_TIER_MIGRATION_BOTTOM: _ClassVar[WebMessageInfo.StubType]
        OVERSIZED: _ClassVar[WebMessageInfo.StubType]
        GROUP_CHANGE_NO_FREQUENTLY_FORWARDED: _ClassVar[WebMessageInfo.StubType]
        GROUP_V4_ADD_INVITE_SENT: _ClassVar[WebMessageInfo.StubType]
        GROUP_PARTICIPANT_ADD_REQUEST_JOIN: _ClassVar[WebMessageInfo.StubType]
        CHANGE_EPHEMERAL_SETTING: _ClassVar[WebMessageInfo.StubType]
        E2E_DEVICE_CHANGED: _ClassVar[WebMessageInfo.StubType]
        VIEWED_ONCE: _ClassVar[WebMessageInfo.StubType]
        E2E_ENCRYPTED_NOW: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_BSP_FB_TO_BSP_PREMISE: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_BSP_FB_TO_SELF_FB: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_BSP_FB_TO_SELF_PREMISE: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_BSP_FB_UNVERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_BSP_FB_UNVERIFIED_TO_SELF_PREMISE_VERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_BSP_FB_VERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_BSP_FB_VERIFIED_TO_SELF_PREMISE_UNVERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_BSP_PREMISE_TO_SELF_PREMISE: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_BSP_PREMISE_UNVERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_BSP_PREMISE_UNVERIFIED_TO_SELF_PREMISE_VERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_BSP_PREMISE_VERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_BSP_PREMISE_VERIFIED_TO_SELF_PREMISE_UNVERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_CONSUMER_TO_BSP_FB_UNVERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_CONSUMER_TO_BSP_PREMISE_UNVERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_CONSUMER_TO_SELF_FB_UNVERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_CONSUMER_TO_SELF_PREMISE_UNVERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_SELF_FB_TO_BSP_PREMISE: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_SELF_FB_TO_SELF_PREMISE: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_SELF_FB_UNVERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_SELF_FB_UNVERIFIED_TO_SELF_PREMISE_VERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_SELF_FB_VERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_SELF_FB_VERIFIED_TO_SELF_PREMISE_UNVERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_SELF_PREMISE_TO_BSP_PREMISE: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_SELF_PREMISE_UNVERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_SELF_PREMISE_VERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_TO_BSP_FB: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_TO_CONSUMER: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_TO_SELF_FB: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_UNVERIFIED_TO_BSP_FB_VERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_UNVERIFIED_TO_BSP_PREMISE_VERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_UNVERIFIED_TO_SELF_FB_VERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_UNVERIFIED_TO_VERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_VERIFIED_TO_BSP_FB_UNVERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_VERIFIED_TO_BSP_PREMISE_UNVERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_VERIFIED_TO_SELF_FB_UNVERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_VERIFIED_TO_UNVERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_BSP_FB_UNVERIFIED_TO_BSP_PREMISE_VERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_BSP_FB_UNVERIFIED_TO_SELF_FB_VERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_BSP_FB_VERIFIED_TO_BSP_PREMISE_UNVERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_BSP_FB_VERIFIED_TO_SELF_FB_UNVERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_SELF_FB_UNVERIFIED_TO_BSP_PREMISE_VERIFIED: _ClassVar[WebMessageInfo.StubType]
        BLUE_MSG_SELF_FB_VERIFIED_TO_BSP_PREMISE_UNVERIFIED: _ClassVar[WebMessageInfo.StubType]
        E2E_IDENTITY_UNAVAILABLE: _ClassVar[WebMessageInfo.StubType]
        GROUP_CREATING: _ClassVar[WebMessageInfo.StubType]
        GROUP_CREATE_FAILED: _ClassVar[WebMessageInfo.StubType]
        GROUP_BOUNCED: _ClassVar[WebMessageInfo.StubType]
        BLOCK_CONTACT: _ClassVar[WebMessageInfo.StubType]
        EPHEMERAL_SETTING_NOT_APPLIED: _ClassVar[WebMessageInfo.StubType]
        SYNC_FAILED: _ClassVar[WebMessageInfo.StubType]
        SYNCING: _ClassVar[WebMessageInfo.StubType]
        BIZ_PRIVACY_MODE_INIT_FB: _ClassVar[WebMessageInfo.StubType]
        BIZ_PRIVACY_MODE_INIT_BSP: _ClassVar[WebMessageInfo.StubType]
        BIZ_PRIVACY_MODE_TO_FB: _ClassVar[WebMessageInfo.StubType]
        BIZ_PRIVACY_MODE_TO_BSP: _ClassVar[WebMessageInfo.StubType]
        DISAPPEARING_MODE: _ClassVar[WebMessageInfo.StubType]
        E2E_DEVICE_FETCH_FAILED: _ClassVar[WebMessageInfo.StubType]
        ADMIN_REVOKE: _ClassVar[WebMessageInfo.StubType]
        GROUP_INVITE_LINK_GROWTH_LOCKED: _ClassVar[WebMessageInfo.StubType]
        COMMUNITY_LINK_PARENT_GROUP: _ClassVar[WebMessageInfo.StubType]
        COMMUNITY_LINK_SIBLING_GROUP: _ClassVar[WebMessageInfo.StubType]
        COMMUNITY_LINK_SUB_GROUP: _ClassVar[WebMessageInfo.StubType]
        COMMUNITY_UNLINK_PARENT_GROUP: _ClassVar[WebMessageInfo.StubType]
        COMMUNITY_UNLINK_SIBLING_GROUP: _ClassVar[WebMessageInfo.StubType]
        COMMUNITY_UNLINK_SUB_GROUP: _ClassVar[WebMessageInfo.StubType]
        GROUP_PARTICIPANT_ACCEPT: _ClassVar[WebMessageInfo.StubType]
        GROUP_PARTICIPANT_LINKED_GROUP_JOIN: _ClassVar[WebMessageInfo.StubType]
        COMMUNITY_CREATE: _ClassVar[WebMessageInfo.StubType]
        EPHEMERAL_KEEP_IN_CHAT: _ClassVar[WebMessageInfo.StubType]
        GROUP_MEMBERSHIP_JOIN_APPROVAL_REQUEST: _ClassVar[WebMessageInfo.StubType]
        GROUP_MEMBERSHIP_JOIN_APPROVAL_MODE: _ClassVar[WebMessageInfo.StubType]
        INTEGRITY_UNLINK_PARENT_GROUP: _ClassVar[WebMessageInfo.StubType]
        COMMUNITY_PARTICIPANT_PROMOTE: _ClassVar[WebMessageInfo.StubType]
        COMMUNITY_PARTICIPANT_DEMOTE: _ClassVar[WebMessageInfo.StubType]
        COMMUNITY_PARENT_GROUP_DELETED: _ClassVar[WebMessageInfo.StubType]
        COMMUNITY_LINK_PARENT_GROUP_MEMBERSHIP_APPROVAL: _ClassVar[WebMessageInfo.StubType]
        GROUP_PARTICIPANT_JOINED_GROUP_AND_PARENT_GROUP: _ClassVar[WebMessageInfo.StubType]
        MASKED_THREAD_CREATED: _ClassVar[WebMessageInfo.StubType]
        MASKED_THREAD_UNMASKED: _ClassVar[WebMessageInfo.StubType]
        BIZ_CHAT_ASSIGNMENT: _ClassVar[WebMessageInfo.StubType]
        CHAT_PSA: _ClassVar[WebMessageInfo.StubType]
        CHAT_POLL_CREATION_MESSAGE: _ClassVar[WebMessageInfo.StubType]
        CAG_MASKED_THREAD_CREATED: _ClassVar[WebMessageInfo.StubType]
        COMMUNITY_PARENT_GROUP_SUBJECT_CHANGED: _ClassVar[WebMessageInfo.StubType]
        CAG_INVITE_AUTO_ADD: _ClassVar[WebMessageInfo.StubType]
        BIZ_CHAT_ASSIGNMENT_UNASSIGN: _ClassVar[WebMessageInfo.StubType]
        CAG_INVITE_AUTO_JOINED: _ClassVar[WebMessageInfo.StubType]
        SCHEDULED_CALL_START_MESSAGE: _ClassVar[WebMessageInfo.StubType]
        COMMUNITY_INVITE_RICH: _ClassVar[WebMessageInfo.StubType]
        COMMUNITY_INVITE_AUTO_ADD_RICH: _ClassVar[WebMessageInfo.StubType]
        SUB_GROUP_INVITE_RICH: _ClassVar[WebMessageInfo.StubType]
        SUB_GROUP_PARTICIPANT_ADD_RICH: _ClassVar[WebMessageInfo.StubType]
        COMMUNITY_LINK_PARENT_GROUP_RICH: _ClassVar[WebMessageInfo.StubType]
        COMMUNITY_PARTICIPANT_ADD_RICH: _ClassVar[WebMessageInfo.StubType]
        SILENCED_UNKNOWN_CALLER_AUDIO: _ClassVar[WebMessageInfo.StubType]
        SILENCED_UNKNOWN_CALLER_VIDEO: _ClassVar[WebMessageInfo.StubType]
        GROUP_MEMBER_ADD_MODE: _ClassVar[WebMessageInfo.StubType]
        GROUP_MEMBERSHIP_JOIN_APPROVAL_REQUEST_NON_ADMIN_ADD: _ClassVar[WebMessageInfo.StubType]
        COMMUNITY_CHANGE_DESCRIPTION: _ClassVar[WebMessageInfo.StubType]
        SENDER_INVITE: _ClassVar[WebMessageInfo.StubType]
        RECEIVER_INVITE: _ClassVar[WebMessageInfo.StubType]
    UNKNOWN: WebMessageInfo.StubType
    REVOKE: WebMessageInfo.StubType
    CIPHERTEXT: WebMessageInfo.StubType
    FUTUREPROOF: WebMessageInfo.StubType
    NON_VERIFIED_TRANSITION: WebMessageInfo.StubType
    UNVERIFIED_TRANSITION: WebMessageInfo.StubType
    VERIFIED_TRANSITION: WebMessageInfo.StubType
    VERIFIED_LOW_UNKNOWN: WebMessageInfo.StubType
    VERIFIED_HIGH: WebMessageInfo.StubType
    VERIFIED_INITIAL_UNKNOWN: WebMessageInfo.StubType
    VERIFIED_INITIAL_LOW: WebMessageInfo.StubType
    VERIFIED_INITIAL_HIGH: WebMessageInfo.StubType
    VERIFIED_TRANSITION_ANY_TO_NONE: WebMessageInfo.StubType
    VERIFIED_TRANSITION_ANY_TO_HIGH: WebMessageInfo.StubType
    VERIFIED_TRANSITION_HIGH_TO_LOW: WebMessageInfo.StubType
    VERIFIED_TRANSITION_HIGH_TO_UNKNOWN: WebMessageInfo.StubType
    VERIFIED_TRANSITION_UNKNOWN_TO_LOW: WebMessageInfo.StubType
    VERIFIED_TRANSITION_LOW_TO_UNKNOWN: WebMessageInfo.StubType
    VERIFIED_TRANSITION_NONE_TO_LOW: WebMessageInfo.StubType
    VERIFIED_TRANSITION_NONE_TO_UNKNOWN: WebMessageInfo.StubType
    GROUP_CREATE: WebMessageInfo.StubType
    GROUP_CHANGE_SUBJECT: WebMessageInfo.StubType
    GROUP_CHANGE_ICON: WebMessageInfo.StubType
    GROUP_CHANGE_INVITE_LINK: WebMessageInfo.StubType
    GROUP_CHANGE_DESCRIPTION: WebMessageInfo.StubType
    GROUP_CHANGE_RESTRICT: WebMessageInfo.StubType
    GROUP_CHANGE_ANNOUNCE: WebMessageInfo.StubType
    GROUP_PARTICIPANT_ADD: WebMessageInfo.StubType
    GROUP_PARTICIPANT_REMOVE: WebMessageInfo.StubType
    GROUP_PARTICIPANT_PROMOTE: WebMessageInfo.StubType
    GROUP_PARTICIPANT_DEMOTE: WebMessageInfo.StubType
    GROUP_PARTICIPANT_INVITE: WebMessageInfo.StubType
    GROUP_PARTICIPANT_LEAVE: WebMessageInfo.StubType
    GROUP_PARTICIPANT_CHANGE_NUMBER: WebMessageInfo.StubType
    BROADCAST_CREATE: WebMessageInfo.StubType
    BROADCAST_ADD: WebMessageInfo.StubType
    BROADCAST_REMOVE: WebMessageInfo.StubType
    GENERIC_NOTIFICATION: WebMessageInfo.StubType
    E2E_IDENTITY_CHANGED: WebMessageInfo.StubType
    E2E_ENCRYPTED: WebMessageInfo.StubType
    CALL_MISSED_VOICE: WebMessageInfo.StubType
    CALL_MISSED_VIDEO: WebMessageInfo.StubType
    INDIVIDUAL_CHANGE_NUMBER: WebMessageInfo.StubType
    GROUP_DELETE: WebMessageInfo.StubType
    GROUP_ANNOUNCE_MODE_MESSAGE_BOUNCE: WebMessageInfo.StubType
    CALL_MISSED_GROUP_VOICE: WebMessageInfo.StubType
    CALL_MISSED_GROUP_VIDEO: WebMessageInfo.StubType
    PAYMENT_CIPHERTEXT: WebMessageInfo.StubType
    PAYMENT_FUTUREPROOF: WebMessageInfo.StubType
    PAYMENT_TRANSACTION_STATUS_UPDATE_FAILED: WebMessageInfo.StubType
    PAYMENT_TRANSACTION_STATUS_UPDATE_REFUNDED: WebMessageInfo.StubType
    PAYMENT_TRANSACTION_STATUS_UPDATE_REFUND_FAILED: WebMessageInfo.StubType
    PAYMENT_TRANSACTION_STATUS_RECEIVER_PENDING_SETUP: WebMessageInfo.StubType
    PAYMENT_TRANSACTION_STATUS_RECEIVER_SUCCESS_AFTER_HICCUP: WebMessageInfo.StubType
    PAYMENT_ACTION_ACCOUNT_SETUP_REMINDER: WebMessageInfo.StubType
    PAYMENT_ACTION_SEND_PAYMENT_REMINDER: WebMessageInfo.StubType
    PAYMENT_ACTION_SEND_PAYMENT_INVITATION: WebMessageInfo.StubType
    PAYMENT_ACTION_REQUEST_DECLINED: WebMessageInfo.StubType
    PAYMENT_ACTION_REQUEST_EXPIRED: WebMessageInfo.StubType
    PAYMENT_ACTION_REQUEST_CANCELLED: WebMessageInfo.StubType
    BIZ_VERIFIED_TRANSITION_TOP_TO_BOTTOM: WebMessageInfo.StubType
    BIZ_VERIFIED_TRANSITION_BOTTOM_TO_TOP: WebMessageInfo.StubType
    BIZ_INTRO_TOP: WebMessageInfo.StubType
    BIZ_INTRO_BOTTOM: WebMessageInfo.StubType
    BIZ_NAME_CHANGE: WebMessageInfo.StubType
    BIZ_MOVE_TO_CONSUMER_APP: WebMessageInfo.StubType
    BIZ_TWO_TIER_MIGRATION_TOP: WebMessageInfo.StubType
    BIZ_TWO_TIER_MIGRATION_BOTTOM: WebMessageInfo.StubType
    OVERSIZED: WebMessageInfo.StubType
    GROUP_CHANGE_NO_FREQUENTLY_FORWARDED: WebMessageInfo.StubType
    GROUP_V4_ADD_INVITE_SENT: WebMessageInfo.StubType
    GROUP_PARTICIPANT_ADD_REQUEST_JOIN: WebMessageInfo.StubType
    CHANGE_EPHEMERAL_SETTING: WebMessageInfo.StubType
    E2E_DEVICE_CHANGED: WebMessageInfo.StubType
    VIEWED_ONCE: WebMessageInfo.StubType
    E2E_ENCRYPTED_NOW: WebMessageInfo.StubType
    BLUE_MSG_BSP_FB_TO_BSP_PREMISE: WebMessageInfo.StubType
    BLUE_MSG_BSP_FB_TO_SELF_FB: WebMessageInfo.StubType
    BLUE_MSG_BSP_FB_TO_SELF_PREMISE: WebMessageInfo.StubType
    BLUE_MSG_BSP_FB_UNVERIFIED: WebMessageInfo.StubType
    BLUE_MSG_BSP_FB_UNVERIFIED_TO_SELF_PREMISE_VERIFIED: WebMessageInfo.StubType
    BLUE_MSG_BSP_FB_VERIFIED: WebMessageInfo.StubType
    BLUE_MSG_BSP_FB_VERIFIED_TO_SELF_PREMISE_UNVERIFIED: WebMessageInfo.StubType
    BLUE_MSG_BSP_PREMISE_TO_SELF_PREMISE: WebMessageInfo.StubType
    BLUE_MSG_BSP_PREMISE_UNVERIFIED: WebMessageInfo.StubType
    BLUE_MSG_BSP_PREMISE_UNVERIFIED_TO_SELF_PREMISE_VERIFIED: WebMessageInfo.StubType
    BLUE_MSG_BSP_PREMISE_VERIFIED: WebMessageInfo.StubType
    BLUE_MSG_BSP_PREMISE_VERIFIED_TO_SELF_PREMISE_UNVERIFIED: WebMessageInfo.StubType
    BLUE_MSG_CONSUMER_TO_BSP_FB_UNVERIFIED: WebMessageInfo.StubType
    BLUE_MSG_CONSUMER_TO_BSP_PREMISE_UNVERIFIED: WebMessageInfo.StubType
    BLUE_MSG_CONSUMER_TO_SELF_FB_UNVERIFIED: WebMessageInfo.StubType
    BLUE_MSG_CONSUMER_TO_SELF_PREMISE_UNVERIFIED: WebMessageInfo.StubType
    BLUE_MSG_SELF_FB_TO_BSP_PREMISE: WebMessageInfo.StubType
    BLUE_MSG_SELF_FB_TO_SELF_PREMISE: WebMessageInfo.StubType
    BLUE_MSG_SELF_FB_UNVERIFIED: WebMessageInfo.StubType
    BLUE_MSG_SELF_FB_UNVERIFIED_TO_SELF_PREMISE_VERIFIED: WebMessageInfo.StubType
    BLUE_MSG_SELF_FB_VERIFIED: WebMessageInfo.StubType
    BLUE_MSG_SELF_FB_VERIFIED_TO_SELF_PREMISE_UNVERIFIED: WebMessageInfo.StubType
    BLUE_MSG_SELF_PREMISE_TO_BSP_PREMISE: WebMessageInfo.StubType
    BLUE_MSG_SELF_PREMISE_UNVERIFIED: WebMessageInfo.StubType
    BLUE_MSG_SELF_PREMISE_VERIFIED: WebMessageInfo.StubType
    BLUE_MSG_TO_BSP_FB: WebMessageInfo.StubType
    BLUE_MSG_TO_CONSUMER: WebMessageInfo.StubType
    BLUE_MSG_TO_SELF_FB: WebMessageInfo.StubType
    BLUE_MSG_UNVERIFIED_TO_BSP_FB_VERIFIED: WebMessageInfo.StubType
    BLUE_MSG_UNVERIFIED_TO_BSP_PREMISE_VERIFIED: WebMessageInfo.StubType
    BLUE_MSG_UNVERIFIED_TO_SELF_FB_VERIFIED: WebMessageInfo.StubType
    BLUE_MSG_UNVERIFIED_TO_VERIFIED: WebMessageInfo.StubType
    BLUE_MSG_VERIFIED_TO_BSP_FB_UNVERIFIED: WebMessageInfo.StubType
    BLUE_MSG_VERIFIED_TO_BSP_PREMISE_UNVERIFIED: WebMessageInfo.StubType
    BLUE_MSG_VERIFIED_TO_SELF_FB_UNVERIFIED: WebMessageInfo.StubType
    BLUE_MSG_VERIFIED_TO_UNVERIFIED: WebMessageInfo.StubType
    BLUE_MSG_BSP_FB_UNVERIFIED_TO_BSP_PREMISE_VERIFIED: WebMessageInfo.StubType
    BLUE_MSG_BSP_FB_UNVERIFIED_TO_SELF_FB_VERIFIED: WebMessageInfo.StubType
    BLUE_MSG_BSP_FB_VERIFIED_TO_BSP_PREMISE_UNVERIFIED: WebMessageInfo.StubType
    BLUE_MSG_BSP_FB_VERIFIED_TO_SELF_FB_UNVERIFIED: WebMessageInfo.StubType
    BLUE_MSG_SELF_FB_UNVERIFIED_TO_BSP_PREMISE_VERIFIED: WebMessageInfo.StubType
    BLUE_MSG_SELF_FB_VERIFIED_TO_BSP_PREMISE_UNVERIFIED: WebMessageInfo.StubType
    E2E_IDENTITY_UNAVAILABLE: WebMessageInfo.StubType
    GROUP_CREATING: WebMessageInfo.StubType
    GROUP_CREATE_FAILED: WebMessageInfo.StubType
    GROUP_BOUNCED: WebMessageInfo.StubType
    BLOCK_CONTACT: WebMessageInfo.StubType
    EPHEMERAL_SETTING_NOT_APPLIED: WebMessageInfo.StubType
    SYNC_FAILED: WebMessageInfo.StubType
    SYNCING: WebMessageInfo.StubType
    BIZ_PRIVACY_MODE_INIT_FB: WebMessageInfo.StubType
    BIZ_PRIVACY_MODE_INIT_BSP: WebMessageInfo.StubType
    BIZ_PRIVACY_MODE_TO_FB: WebMessageInfo.StubType
    BIZ_PRIVACY_MODE_TO_BSP: WebMessageInfo.StubType
    DISAPPEARING_MODE: WebMessageInfo.StubType
    E2E_DEVICE_FETCH_FAILED: WebMessageInfo.StubType
    ADMIN_REVOKE: WebMessageInfo.StubType
    GROUP_INVITE_LINK_GROWTH_LOCKED: WebMessageInfo.StubType
    COMMUNITY_LINK_PARENT_GROUP: WebMessageInfo.StubType
    COMMUNITY_LINK_SIBLING_GROUP: WebMessageInfo.StubType
    COMMUNITY_LINK_SUB_GROUP: WebMessageInfo.StubType
    COMMUNITY_UNLINK_PARENT_GROUP: WebMessageInfo.StubType
    COMMUNITY_UNLINK_SIBLING_GROUP: WebMessageInfo.StubType
    COMMUNITY_UNLINK_SUB_GROUP: WebMessageInfo.StubType
    GROUP_PARTICIPANT_ACCEPT: WebMessageInfo.StubType
    GROUP_PARTICIPANT_LINKED_GROUP_JOIN: WebMessageInfo.StubType
    COMMUNITY_CREATE: WebMessageInfo.StubType
    EPHEMERAL_KEEP_IN_CHAT: WebMessageInfo.StubType
    GROUP_MEMBERSHIP_JOIN_APPROVAL_REQUEST: WebMessageInfo.StubType
    GROUP_MEMBERSHIP_JOIN_APPROVAL_MODE: WebMessageInfo.StubType
    INTEGRITY_UNLINK_PARENT_GROUP: WebMessageInfo.StubType
    COMMUNITY_PARTICIPANT_PROMOTE: WebMessageInfo.StubType
    COMMUNITY_PARTICIPANT_DEMOTE: WebMessageInfo.StubType
    COMMUNITY_PARENT_GROUP_DELETED: WebMessageInfo.StubType
    COMMUNITY_LINK_PARENT_GROUP_MEMBERSHIP_APPROVAL: WebMessageInfo.StubType
    GROUP_PARTICIPANT_JOINED_GROUP_AND_PARENT_GROUP: WebMessageInfo.StubType
    MASKED_THREAD_CREATED: WebMessageInfo.StubType
    MASKED_THREAD_UNMASKED: WebMessageInfo.StubType
    BIZ_CHAT_ASSIGNMENT: WebMessageInfo.StubType
    CHAT_PSA: WebMessageInfo.StubType
    CHAT_POLL_CREATION_MESSAGE: WebMessageInfo.StubType
    CAG_MASKED_THREAD_CREATED: WebMessageInfo.StubType
    COMMUNITY_PARENT_GROUP_SUBJECT_CHANGED: WebMessageInfo.StubType
    CAG_INVITE_AUTO_ADD: WebMessageInfo.StubType
    BIZ_CHAT_ASSIGNMENT_UNASSIGN: WebMessageInfo.StubType
    CAG_INVITE_AUTO_JOINED: WebMessageInfo.StubType
    SCHEDULED_CALL_START_MESSAGE: WebMessageInfo.StubType
    COMMUNITY_INVITE_RICH: WebMessageInfo.StubType
    COMMUNITY_INVITE_AUTO_ADD_RICH: WebMessageInfo.StubType
    SUB_GROUP_INVITE_RICH: WebMessageInfo.StubType
    SUB_GROUP_PARTICIPANT_ADD_RICH: WebMessageInfo.StubType
    COMMUNITY_LINK_PARENT_GROUP_RICH: WebMessageInfo.StubType
    COMMUNITY_PARTICIPANT_ADD_RICH: WebMessageInfo.StubType
    SILENCED_UNKNOWN_CALLER_AUDIO: WebMessageInfo.StubType
    SILENCED_UNKNOWN_CALLER_VIDEO: WebMessageInfo.StubType
    GROUP_MEMBER_ADD_MODE: WebMessageInfo.StubType
    GROUP_MEMBERSHIP_JOIN_APPROVAL_REQUEST_NON_ADMIN_ADD: WebMessageInfo.StubType
    COMMUNITY_CHANGE_DESCRIPTION: WebMessageInfo.StubType
    SENDER_INVITE: WebMessageInfo.StubType
    RECEIVER_INVITE: WebMessageInfo.StubType
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        ERROR: _ClassVar[WebMessageInfo.Status]
        PENDING: _ClassVar[WebMessageInfo.Status]
        SERVER_ACK: _ClassVar[WebMessageInfo.Status]
        DELIVERY_ACK: _ClassVar[WebMessageInfo.Status]
        READ: _ClassVar[WebMessageInfo.Status]
        PLAYED: _ClassVar[WebMessageInfo.Status]
    ERROR: WebMessageInfo.Status
    PENDING: WebMessageInfo.Status
    SERVER_ACK: WebMessageInfo.Status
    DELIVERY_ACK: WebMessageInfo.Status
    READ: WebMessageInfo.Status
    PLAYED: WebMessageInfo.Status
    class BizPrivacyStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        E2EE: _ClassVar[WebMessageInfo.BizPrivacyStatus]
        FB: _ClassVar[WebMessageInfo.BizPrivacyStatus]
        BSP: _ClassVar[WebMessageInfo.BizPrivacyStatus]
        BSP_AND_FB: _ClassVar[WebMessageInfo.BizPrivacyStatus]
    E2EE: WebMessageInfo.BizPrivacyStatus
    FB: WebMessageInfo.BizPrivacyStatus
    BSP: WebMessageInfo.BizPrivacyStatus
    BSP_AND_FB: WebMessageInfo.BizPrivacyStatus
    KEY_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGETIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    MESSAGEC2STIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    IGNORE_FIELD_NUMBER: _ClassVar[int]
    STARRED_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_FIELD_NUMBER: _ClassVar[int]
    PUSHNAME_FIELD_NUMBER: _ClassVar[int]
    MEDIACIPHERTEXTSHA256_FIELD_NUMBER: _ClassVar[int]
    MULTICAST_FIELD_NUMBER: _ClassVar[int]
    URLTEXT_FIELD_NUMBER: _ClassVar[int]
    URLNUMBER_FIELD_NUMBER: _ClassVar[int]
    MESSAGESTUBTYPE_FIELD_NUMBER: _ClassVar[int]
    CLEARMEDIA_FIELD_NUMBER: _ClassVar[int]
    MESSAGESTUBPARAMETERS_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    PAYMENTINFO_FIELD_NUMBER: _ClassVar[int]
    FINALLIVELOCATION_FIELD_NUMBER: _ClassVar[int]
    QUOTEDPAYMENTINFO_FIELD_NUMBER: _ClassVar[int]
    EPHEMERALSTARTTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EPHEMERALDURATION_FIELD_NUMBER: _ClassVar[int]
    EPHEMERALOFFTOON_FIELD_NUMBER: _ClassVar[int]
    EPHEMERALOUTOFSYNC_FIELD_NUMBER: _ClassVar[int]
    BIZPRIVACYSTATUS_FIELD_NUMBER: _ClassVar[int]
    VERIFIEDBIZNAME_FIELD_NUMBER: _ClassVar[int]
    MEDIADATA_FIELD_NUMBER: _ClassVar[int]
    PHOTOCHANGE_FIELD_NUMBER: _ClassVar[int]
    USERRECEIPT_FIELD_NUMBER: _ClassVar[int]
    REACTIONS_FIELD_NUMBER: _ClassVar[int]
    QUOTEDSTICKERDATA_FIELD_NUMBER: _ClassVar[int]
    FUTUREPROOFDATA_FIELD_NUMBER: _ClassVar[int]
    STATUSPSA_FIELD_NUMBER: _ClassVar[int]
    POLLUPDATES_FIELD_NUMBER: _ClassVar[int]
    POLLADDITIONALMETADATA_FIELD_NUMBER: _ClassVar[int]
    AGENTID_FIELD_NUMBER: _ClassVar[int]
    STATUSALREADYVIEWED_FIELD_NUMBER: _ClassVar[int]
    MESSAGESECRET_FIELD_NUMBER: _ClassVar[int]
    KEEPINCHAT_FIELD_NUMBER: _ClassVar[int]
    ORIGINALSELFAUTHORUSERJIDSTRING_FIELD_NUMBER: _ClassVar[int]
    REVOKEMESSAGETIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    key: MessageKey
    message: Message
    messageTimestamp: int
    status: WebMessageInfo.Status
    participant: str
    messageC2STimestamp: int
    ignore: bool
    starred: bool
    broadcast: bool
    pushName: str
    mediaCiphertextSha256: bytes
    multicast: bool
    urlText: bool
    urlNumber: bool
    messageStubType: WebMessageInfo.StubType
    clearMedia: bool
    messageStubParameters: _containers.RepeatedScalarFieldContainer[str]
    duration: int
    labels: _containers.RepeatedScalarFieldContainer[str]
    paymentInfo: PaymentInfo
    finalLiveLocation: LiveLocationMessage
    quotedPaymentInfo: PaymentInfo
    ephemeralStartTimestamp: int
    ephemeralDuration: int
    ephemeralOffToOn: bool
    ephemeralOutOfSync: bool
    bizPrivacyStatus: WebMessageInfo.BizPrivacyStatus
    verifiedBizName: str
    mediaData: MediaData
    photoChange: PhotoChange
    userReceipt: _containers.RepeatedCompositeFieldContainer[UserReceipt]
    reactions: _containers.RepeatedCompositeFieldContainer[Reaction]
    quotedStickerData: MediaData
    futureproofData: bytes
    statusPsa: StatusPSA
    pollUpdates: _containers.RepeatedCompositeFieldContainer[PollUpdate]
    pollAdditionalMetadata: PollAdditionalMetadata
    agentId: str
    statusAlreadyViewed: bool
    messageSecret: bytes
    keepInChat: KeepInChat
    originalSelfAuthorUserJidString: str
    revokeMessageTimestamp: int
    def __init__(self, key: _Optional[_Union[MessageKey, _Mapping]] = ..., message: _Optional[_Union[Message, _Mapping]] = ..., messageTimestamp: _Optional[int] = ..., status: _Optional[_Union[WebMessageInfo.Status, str]] = ..., participant: _Optional[str] = ..., messageC2STimestamp: _Optional[int] = ..., ignore: bool = ..., starred: bool = ..., broadcast: bool = ..., pushName: _Optional[str] = ..., mediaCiphertextSha256: _Optional[bytes] = ..., multicast: bool = ..., urlText: bool = ..., urlNumber: bool = ..., messageStubType: _Optional[_Union[WebMessageInfo.StubType, str]] = ..., clearMedia: bool = ..., messageStubParameters: _Optional[_Iterable[str]] = ..., duration: _Optional[int] = ..., labels: _Optional[_Iterable[str]] = ..., paymentInfo: _Optional[_Union[PaymentInfo, _Mapping]] = ..., finalLiveLocation: _Optional[_Union[LiveLocationMessage, _Mapping]] = ..., quotedPaymentInfo: _Optional[_Union[PaymentInfo, _Mapping]] = ..., ephemeralStartTimestamp: _Optional[int] = ..., ephemeralDuration: _Optional[int] = ..., ephemeralOffToOn: bool = ..., ephemeralOutOfSync: bool = ..., bizPrivacyStatus: _Optional[_Union[WebMessageInfo.BizPrivacyStatus, str]] = ..., verifiedBizName: _Optional[str] = ..., mediaData: _Optional[_Union[MediaData, _Mapping]] = ..., photoChange: _Optional[_Union[PhotoChange, _Mapping]] = ..., userReceipt: _Optional[_Iterable[_Union[UserReceipt, _Mapping]]] = ..., reactions: _Optional[_Iterable[_Union[Reaction, _Mapping]]] = ..., quotedStickerData: _Optional[_Union[MediaData, _Mapping]] = ..., futureproofData: _Optional[bytes] = ..., statusPsa: _Optional[_Union[StatusPSA, _Mapping]] = ..., pollUpdates: _Optional[_Iterable[_Union[PollUpdate, _Mapping]]] = ..., pollAdditionalMetadata: _Optional[_Union[PollAdditionalMetadata, _Mapping]] = ..., agentId: _Optional[str] = ..., statusAlreadyViewed: bool = ..., messageSecret: _Optional[bytes] = ..., keepInChat: _Optional[_Union[KeepInChat, _Mapping]] = ..., originalSelfAuthorUserJidString: _Optional[str] = ..., revokeMessageTimestamp: _Optional[int] = ...) -> None: ...

class WebFeatures(_message.Message):
    __slots__ = ["labelsDisplay", "voipIndividualOutgoing", "groupsV3", "groupsV3Create", "changeNumberV2", "queryStatusV3Thumbnail", "liveLocations", "queryVname", "voipIndividualIncoming", "quickRepliesQuery", "payments", "stickerPackQuery", "liveLocationsFinal", "labelsEdit", "mediaUpload", "mediaUploadRichQuickReplies", "vnameV2", "videoPlaybackUrl", "statusRanking", "voipIndividualVideo", "thirdPartyStickers", "frequentlyForwardedSetting", "groupsV4JoinPermission", "recentStickers", "catalog", "starredStickers", "voipGroupCall", "templateMessage", "templateMessageInteractivity", "ephemeralMessages", "e2ENotificationSync", "recentStickersV2", "recentStickersV3", "userNotice", "support", "groupUiiCleanup", "groupDogfoodingInternalOnly", "settingsSync", "archiveV2", "ephemeralAllowGroupMembers", "ephemeral24HDuration", "mdForceUpgrade", "disappearingMode", "externalMdOptInAvailable", "noDeleteMessageTimeLimit"]
    class Flag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        NOT_STARTED: _ClassVar[WebFeatures.Flag]
        FORCE_UPGRADE: _ClassVar[WebFeatures.Flag]
        DEVELOPMENT: _ClassVar[WebFeatures.Flag]
        PRODUCTION: _ClassVar[WebFeatures.Flag]
    NOT_STARTED: WebFeatures.Flag
    FORCE_UPGRADE: WebFeatures.Flag
    DEVELOPMENT: WebFeatures.Flag
    PRODUCTION: WebFeatures.Flag
    LABELSDISPLAY_FIELD_NUMBER: _ClassVar[int]
    VOIPINDIVIDUALOUTGOING_FIELD_NUMBER: _ClassVar[int]
    GROUPSV3_FIELD_NUMBER: _ClassVar[int]
    GROUPSV3CREATE_FIELD_NUMBER: _ClassVar[int]
    CHANGENUMBERV2_FIELD_NUMBER: _ClassVar[int]
    QUERYSTATUSV3THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    LIVELOCATIONS_FIELD_NUMBER: _ClassVar[int]
    QUERYVNAME_FIELD_NUMBER: _ClassVar[int]
    VOIPINDIVIDUALINCOMING_FIELD_NUMBER: _ClassVar[int]
    QUICKREPLIESQUERY_FIELD_NUMBER: _ClassVar[int]
    PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    STICKERPACKQUERY_FIELD_NUMBER: _ClassVar[int]
    LIVELOCATIONSFINAL_FIELD_NUMBER: _ClassVar[int]
    LABELSEDIT_FIELD_NUMBER: _ClassVar[int]
    MEDIAUPLOAD_FIELD_NUMBER: _ClassVar[int]
    MEDIAUPLOADRICHQUICKREPLIES_FIELD_NUMBER: _ClassVar[int]
    VNAMEV2_FIELD_NUMBER: _ClassVar[int]
    VIDEOPLAYBACKURL_FIELD_NUMBER: _ClassVar[int]
    STATUSRANKING_FIELD_NUMBER: _ClassVar[int]
    VOIPINDIVIDUALVIDEO_FIELD_NUMBER: _ClassVar[int]
    THIRDPARTYSTICKERS_FIELD_NUMBER: _ClassVar[int]
    FREQUENTLYFORWARDEDSETTING_FIELD_NUMBER: _ClassVar[int]
    GROUPSV4JOINPERMISSION_FIELD_NUMBER: _ClassVar[int]
    RECENTSTICKERS_FIELD_NUMBER: _ClassVar[int]
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    STARREDSTICKERS_FIELD_NUMBER: _ClassVar[int]
    VOIPGROUPCALL_FIELD_NUMBER: _ClassVar[int]
    TEMPLATEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATEMESSAGEINTERACTIVITY_FIELD_NUMBER: _ClassVar[int]
    EPHEMERALMESSAGES_FIELD_NUMBER: _ClassVar[int]
    E2ENOTIFICATIONSYNC_FIELD_NUMBER: _ClassVar[int]
    RECENTSTICKERSV2_FIELD_NUMBER: _ClassVar[int]
    RECENTSTICKERSV3_FIELD_NUMBER: _ClassVar[int]
    USERNOTICE_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_FIELD_NUMBER: _ClassVar[int]
    GROUPUIICLEANUP_FIELD_NUMBER: _ClassVar[int]
    GROUPDOGFOODINGINTERNALONLY_FIELD_NUMBER: _ClassVar[int]
    SETTINGSSYNC_FIELD_NUMBER: _ClassVar[int]
    ARCHIVEV2_FIELD_NUMBER: _ClassVar[int]
    EPHEMERALALLOWGROUPMEMBERS_FIELD_NUMBER: _ClassVar[int]
    EPHEMERAL24HDURATION_FIELD_NUMBER: _ClassVar[int]
    MDFORCEUPGRADE_FIELD_NUMBER: _ClassVar[int]
    DISAPPEARINGMODE_FIELD_NUMBER: _ClassVar[int]
    EXTERNALMDOPTINAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    NODELETEMESSAGETIMELIMIT_FIELD_NUMBER: _ClassVar[int]
    labelsDisplay: WebFeatures.Flag
    voipIndividualOutgoing: WebFeatures.Flag
    groupsV3: WebFeatures.Flag
    groupsV3Create: WebFeatures.Flag
    changeNumberV2: WebFeatures.Flag
    queryStatusV3Thumbnail: WebFeatures.Flag
    liveLocations: WebFeatures.Flag
    queryVname: WebFeatures.Flag
    voipIndividualIncoming: WebFeatures.Flag
    quickRepliesQuery: WebFeatures.Flag
    payments: WebFeatures.Flag
    stickerPackQuery: WebFeatures.Flag
    liveLocationsFinal: WebFeatures.Flag
    labelsEdit: WebFeatures.Flag
    mediaUpload: WebFeatures.Flag
    mediaUploadRichQuickReplies: WebFeatures.Flag
    vnameV2: WebFeatures.Flag
    videoPlaybackUrl: WebFeatures.Flag
    statusRanking: WebFeatures.Flag
    voipIndividualVideo: WebFeatures.Flag
    thirdPartyStickers: WebFeatures.Flag
    frequentlyForwardedSetting: WebFeatures.Flag
    groupsV4JoinPermission: WebFeatures.Flag
    recentStickers: WebFeatures.Flag
    catalog: WebFeatures.Flag
    starredStickers: WebFeatures.Flag
    voipGroupCall: WebFeatures.Flag
    templateMessage: WebFeatures.Flag
    templateMessageInteractivity: WebFeatures.Flag
    ephemeralMessages: WebFeatures.Flag
    e2ENotificationSync: WebFeatures.Flag
    recentStickersV2: WebFeatures.Flag
    recentStickersV3: WebFeatures.Flag
    userNotice: WebFeatures.Flag
    support: WebFeatures.Flag
    groupUiiCleanup: WebFeatures.Flag
    groupDogfoodingInternalOnly: WebFeatures.Flag
    settingsSync: WebFeatures.Flag
    archiveV2: WebFeatures.Flag
    ephemeralAllowGroupMembers: WebFeatures.Flag
    ephemeral24HDuration: WebFeatures.Flag
    mdForceUpgrade: WebFeatures.Flag
    disappearingMode: WebFeatures.Flag
    externalMdOptInAvailable: WebFeatures.Flag
    noDeleteMessageTimeLimit: WebFeatures.Flag
    def __init__(self, labelsDisplay: _Optional[_Union[WebFeatures.Flag, str]] = ..., voipIndividualOutgoing: _Optional[_Union[WebFeatures.Flag, str]] = ..., groupsV3: _Optional[_Union[WebFeatures.Flag, str]] = ..., groupsV3Create: _Optional[_Union[WebFeatures.Flag, str]] = ..., changeNumberV2: _Optional[_Union[WebFeatures.Flag, str]] = ..., queryStatusV3Thumbnail: _Optional[_Union[WebFeatures.Flag, str]] = ..., liveLocations: _Optional[_Union[WebFeatures.Flag, str]] = ..., queryVname: _Optional[_Union[WebFeatures.Flag, str]] = ..., voipIndividualIncoming: _Optional[_Union[WebFeatures.Flag, str]] = ..., quickRepliesQuery: _Optional[_Union[WebFeatures.Flag, str]] = ..., payments: _Optional[_Union[WebFeatures.Flag, str]] = ..., stickerPackQuery: _Optional[_Union[WebFeatures.Flag, str]] = ..., liveLocationsFinal: _Optional[_Union[WebFeatures.Flag, str]] = ..., labelsEdit: _Optional[_Union[WebFeatures.Flag, str]] = ..., mediaUpload: _Optional[_Union[WebFeatures.Flag, str]] = ..., mediaUploadRichQuickReplies: _Optional[_Union[WebFeatures.Flag, str]] = ..., vnameV2: _Optional[_Union[WebFeatures.Flag, str]] = ..., videoPlaybackUrl: _Optional[_Union[WebFeatures.Flag, str]] = ..., statusRanking: _Optional[_Union[WebFeatures.Flag, str]] = ..., voipIndividualVideo: _Optional[_Union[WebFeatures.Flag, str]] = ..., thirdPartyStickers: _Optional[_Union[WebFeatures.Flag, str]] = ..., frequentlyForwardedSetting: _Optional[_Union[WebFeatures.Flag, str]] = ..., groupsV4JoinPermission: _Optional[_Union[WebFeatures.Flag, str]] = ..., recentStickers: _Optional[_Union[WebFeatures.Flag, str]] = ..., catalog: _Optional[_Union[WebFeatures.Flag, str]] = ..., starredStickers: _Optional[_Union[WebFeatures.Flag, str]] = ..., voipGroupCall: _Optional[_Union[WebFeatures.Flag, str]] = ..., templateMessage: _Optional[_Union[WebFeatures.Flag, str]] = ..., templateMessageInteractivity: _Optional[_Union[WebFeatures.Flag, str]] = ..., ephemeralMessages: _Optional[_Union[WebFeatures.Flag, str]] = ..., e2ENotificationSync: _Optional[_Union[WebFeatures.Flag, str]] = ..., recentStickersV2: _Optional[_Union[WebFeatures.Flag, str]] = ..., recentStickersV3: _Optional[_Union[WebFeatures.Flag, str]] = ..., userNotice: _Optional[_Union[WebFeatures.Flag, str]] = ..., support: _Optional[_Union[WebFeatures.Flag, str]] = ..., groupUiiCleanup: _Optional[_Union[WebFeatures.Flag, str]] = ..., groupDogfoodingInternalOnly: _Optional[_Union[WebFeatures.Flag, str]] = ..., settingsSync: _Optional[_Union[WebFeatures.Flag, str]] = ..., archiveV2: _Optional[_Union[WebFeatures.Flag, str]] = ..., ephemeralAllowGroupMembers: _Optional[_Union[WebFeatures.Flag, str]] = ..., ephemeral24HDuration: _Optional[_Union[WebFeatures.Flag, str]] = ..., mdForceUpgrade: _Optional[_Union[WebFeatures.Flag, str]] = ..., disappearingMode: _Optional[_Union[WebFeatures.Flag, str]] = ..., externalMdOptInAvailable: _Optional[_Union[WebFeatures.Flag, str]] = ..., noDeleteMessageTimeLimit: _Optional[_Union[WebFeatures.Flag, str]] = ...) -> None: ...

class UserReceipt(_message.Message):
    __slots__ = ["userJid", "receiptTimestamp", "readTimestamp", "playedTimestamp", "pendingDeviceJid", "deliveredDeviceJid"]
    USERJID_FIELD_NUMBER: _ClassVar[int]
    RECEIPTTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    READTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PLAYEDTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PENDINGDEVICEJID_FIELD_NUMBER: _ClassVar[int]
    DELIVEREDDEVICEJID_FIELD_NUMBER: _ClassVar[int]
    userJid: str
    receiptTimestamp: int
    readTimestamp: int
    playedTimestamp: int
    pendingDeviceJid: _containers.RepeatedScalarFieldContainer[str]
    deliveredDeviceJid: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, userJid: _Optional[str] = ..., receiptTimestamp: _Optional[int] = ..., readTimestamp: _Optional[int] = ..., playedTimestamp: _Optional[int] = ..., pendingDeviceJid: _Optional[_Iterable[str]] = ..., deliveredDeviceJid: _Optional[_Iterable[str]] = ...) -> None: ...

class StatusPSA(_message.Message):
    __slots__ = ["campaignId", "campaignExpirationTimestamp"]
    CAMPAIGNID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGNEXPIRATIONTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    campaignId: int
    campaignExpirationTimestamp: int
    def __init__(self, campaignId: _Optional[int] = ..., campaignExpirationTimestamp: _Optional[int] = ...) -> None: ...

class Reaction(_message.Message):
    __slots__ = ["key", "text", "groupingKey", "senderTimestampMs", "unread"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    GROUPINGKEY_FIELD_NUMBER: _ClassVar[int]
    SENDERTIMESTAMPMS_FIELD_NUMBER: _ClassVar[int]
    UNREAD_FIELD_NUMBER: _ClassVar[int]
    key: MessageKey
    text: str
    groupingKey: str
    senderTimestampMs: int
    unread: bool
    def __init__(self, key: _Optional[_Union[MessageKey, _Mapping]] = ..., text: _Optional[str] = ..., groupingKey: _Optional[str] = ..., senderTimestampMs: _Optional[int] = ..., unread: bool = ...) -> None: ...

class PollUpdate(_message.Message):
    __slots__ = ["pollUpdateMessageKey", "vote", "senderTimestampMs", "serverTimestampMs", "unread"]
    POLLUPDATEMESSAGEKEY_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    SENDERTIMESTAMPMS_FIELD_NUMBER: _ClassVar[int]
    SERVERTIMESTAMPMS_FIELD_NUMBER: _ClassVar[int]
    UNREAD_FIELD_NUMBER: _ClassVar[int]
    pollUpdateMessageKey: MessageKey
    vote: PollVoteMessage
    senderTimestampMs: int
    serverTimestampMs: int
    unread: bool
    def __init__(self, pollUpdateMessageKey: _Optional[_Union[MessageKey, _Mapping]] = ..., vote: _Optional[_Union[PollVoteMessage, _Mapping]] = ..., senderTimestampMs: _Optional[int] = ..., serverTimestampMs: _Optional[int] = ..., unread: bool = ...) -> None: ...

class PollAdditionalMetadata(_message.Message):
    __slots__ = ["pollInvalidated"]
    POLLINVALIDATED_FIELD_NUMBER: _ClassVar[int]
    pollInvalidated: bool
    def __init__(self, pollInvalidated: bool = ...) -> None: ...

class PhotoChange(_message.Message):
    __slots__ = ["oldPhoto", "newPhoto", "newPhotoId"]
    OLDPHOTO_FIELD_NUMBER: _ClassVar[int]
    NEWPHOTO_FIELD_NUMBER: _ClassVar[int]
    NEWPHOTOID_FIELD_NUMBER: _ClassVar[int]
    oldPhoto: bytes
    newPhoto: bytes
    newPhotoId: int
    def __init__(self, oldPhoto: _Optional[bytes] = ..., newPhoto: _Optional[bytes] = ..., newPhotoId: _Optional[int] = ...) -> None: ...

class PaymentInfo(_message.Message):
    __slots__ = ["currencyDeprecated", "amount1000", "receiverJid", "status", "transactionTimestamp", "requestMessageKey", "expiryTimestamp", "futureproofed", "currency", "txnStatus", "useNoviFiatFormat", "primaryAmount", "exchangeAmount"]
    class TxnStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[PaymentInfo.TxnStatus]
        PENDING_SETUP: _ClassVar[PaymentInfo.TxnStatus]
        PENDING_RECEIVER_SETUP: _ClassVar[PaymentInfo.TxnStatus]
        INIT: _ClassVar[PaymentInfo.TxnStatus]
        SUCCESS: _ClassVar[PaymentInfo.TxnStatus]
        COMPLETED: _ClassVar[PaymentInfo.TxnStatus]
        FAILED: _ClassVar[PaymentInfo.TxnStatus]
        FAILED_RISK: _ClassVar[PaymentInfo.TxnStatus]
        FAILED_PROCESSING: _ClassVar[PaymentInfo.TxnStatus]
        FAILED_RECEIVER_PROCESSING: _ClassVar[PaymentInfo.TxnStatus]
        FAILED_DA: _ClassVar[PaymentInfo.TxnStatus]
        FAILED_DA_FINAL: _ClassVar[PaymentInfo.TxnStatus]
        REFUNDED_TXN: _ClassVar[PaymentInfo.TxnStatus]
        REFUND_FAILED: _ClassVar[PaymentInfo.TxnStatus]
        REFUND_FAILED_PROCESSING: _ClassVar[PaymentInfo.TxnStatus]
        REFUND_FAILED_DA: _ClassVar[PaymentInfo.TxnStatus]
        EXPIRED_TXN: _ClassVar[PaymentInfo.TxnStatus]
        AUTH_CANCELED: _ClassVar[PaymentInfo.TxnStatus]
        AUTH_CANCEL_FAILED_PROCESSING: _ClassVar[PaymentInfo.TxnStatus]
        AUTH_CANCEL_FAILED: _ClassVar[PaymentInfo.TxnStatus]
        COLLECT_INIT: _ClassVar[PaymentInfo.TxnStatus]
        COLLECT_SUCCESS: _ClassVar[PaymentInfo.TxnStatus]
        COLLECT_FAILED: _ClassVar[PaymentInfo.TxnStatus]
        COLLECT_FAILED_RISK: _ClassVar[PaymentInfo.TxnStatus]
        COLLECT_REJECTED: _ClassVar[PaymentInfo.TxnStatus]
        COLLECT_EXPIRED: _ClassVar[PaymentInfo.TxnStatus]
        COLLECT_CANCELED: _ClassVar[PaymentInfo.TxnStatus]
        COLLECT_CANCELLING: _ClassVar[PaymentInfo.TxnStatus]
        IN_REVIEW: _ClassVar[PaymentInfo.TxnStatus]
        REVERSAL_SUCCESS: _ClassVar[PaymentInfo.TxnStatus]
        REVERSAL_PENDING: _ClassVar[PaymentInfo.TxnStatus]
        REFUND_PENDING: _ClassVar[PaymentInfo.TxnStatus]
    UNKNOWN: PaymentInfo.TxnStatus
    PENDING_SETUP: PaymentInfo.TxnStatus
    PENDING_RECEIVER_SETUP: PaymentInfo.TxnStatus
    INIT: PaymentInfo.TxnStatus
    SUCCESS: PaymentInfo.TxnStatus
    COMPLETED: PaymentInfo.TxnStatus
    FAILED: PaymentInfo.TxnStatus
    FAILED_RISK: PaymentInfo.TxnStatus
    FAILED_PROCESSING: PaymentInfo.TxnStatus
    FAILED_RECEIVER_PROCESSING: PaymentInfo.TxnStatus
    FAILED_DA: PaymentInfo.TxnStatus
    FAILED_DA_FINAL: PaymentInfo.TxnStatus
    REFUNDED_TXN: PaymentInfo.TxnStatus
    REFUND_FAILED: PaymentInfo.TxnStatus
    REFUND_FAILED_PROCESSING: PaymentInfo.TxnStatus
    REFUND_FAILED_DA: PaymentInfo.TxnStatus
    EXPIRED_TXN: PaymentInfo.TxnStatus
    AUTH_CANCELED: PaymentInfo.TxnStatus
    AUTH_CANCEL_FAILED_PROCESSING: PaymentInfo.TxnStatus
    AUTH_CANCEL_FAILED: PaymentInfo.TxnStatus
    COLLECT_INIT: PaymentInfo.TxnStatus
    COLLECT_SUCCESS: PaymentInfo.TxnStatus
    COLLECT_FAILED: PaymentInfo.TxnStatus
    COLLECT_FAILED_RISK: PaymentInfo.TxnStatus
    COLLECT_REJECTED: PaymentInfo.TxnStatus
    COLLECT_EXPIRED: PaymentInfo.TxnStatus
    COLLECT_CANCELED: PaymentInfo.TxnStatus
    COLLECT_CANCELLING: PaymentInfo.TxnStatus
    IN_REVIEW: PaymentInfo.TxnStatus
    REVERSAL_SUCCESS: PaymentInfo.TxnStatus
    REVERSAL_PENDING: PaymentInfo.TxnStatus
    REFUND_PENDING: PaymentInfo.TxnStatus
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN_STATUS: _ClassVar[PaymentInfo.Status]
        PROCESSING: _ClassVar[PaymentInfo.Status]
        SENT: _ClassVar[PaymentInfo.Status]
        NEED_TO_ACCEPT: _ClassVar[PaymentInfo.Status]
        COMPLETE: _ClassVar[PaymentInfo.Status]
        COULD_NOT_COMPLETE: _ClassVar[PaymentInfo.Status]
        REFUNDED: _ClassVar[PaymentInfo.Status]
        EXPIRED: _ClassVar[PaymentInfo.Status]
        REJECTED: _ClassVar[PaymentInfo.Status]
        CANCELLED: _ClassVar[PaymentInfo.Status]
        WAITING_FOR_PAYER: _ClassVar[PaymentInfo.Status]
        WAITING: _ClassVar[PaymentInfo.Status]
    UNKNOWN_STATUS: PaymentInfo.Status
    PROCESSING: PaymentInfo.Status
    SENT: PaymentInfo.Status
    NEED_TO_ACCEPT: PaymentInfo.Status
    COMPLETE: PaymentInfo.Status
    COULD_NOT_COMPLETE: PaymentInfo.Status
    REFUNDED: PaymentInfo.Status
    EXPIRED: PaymentInfo.Status
    REJECTED: PaymentInfo.Status
    CANCELLED: PaymentInfo.Status
    WAITING_FOR_PAYER: PaymentInfo.Status
    WAITING: PaymentInfo.Status
    class Currency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN_CURRENCY: _ClassVar[PaymentInfo.Currency]
        INR: _ClassVar[PaymentInfo.Currency]
    UNKNOWN_CURRENCY: PaymentInfo.Currency
    INR: PaymentInfo.Currency
    CURRENCYDEPRECATED_FIELD_NUMBER: _ClassVar[int]
    AMOUNT1000_FIELD_NUMBER: _ClassVar[int]
    RECEIVERJID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    REQUESTMESSAGEKEY_FIELD_NUMBER: _ClassVar[int]
    EXPIRYTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    FUTUREPROOFED_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    TXNSTATUS_FIELD_NUMBER: _ClassVar[int]
    USENOVIFIATFORMAT_FIELD_NUMBER: _ClassVar[int]
    PRIMARYAMOUNT_FIELD_NUMBER: _ClassVar[int]
    EXCHANGEAMOUNT_FIELD_NUMBER: _ClassVar[int]
    currencyDeprecated: PaymentInfo.Currency
    amount1000: int
    receiverJid: str
    status: PaymentInfo.Status
    transactionTimestamp: int
    requestMessageKey: MessageKey
    expiryTimestamp: int
    futureproofed: bool
    currency: str
    txnStatus: PaymentInfo.TxnStatus
    useNoviFiatFormat: bool
    primaryAmount: Money
    exchangeAmount: Money
    def __init__(self, currencyDeprecated: _Optional[_Union[PaymentInfo.Currency, str]] = ..., amount1000: _Optional[int] = ..., receiverJid: _Optional[str] = ..., status: _Optional[_Union[PaymentInfo.Status, str]] = ..., transactionTimestamp: _Optional[int] = ..., requestMessageKey: _Optional[_Union[MessageKey, _Mapping]] = ..., expiryTimestamp: _Optional[int] = ..., futureproofed: bool = ..., currency: _Optional[str] = ..., txnStatus: _Optional[_Union[PaymentInfo.TxnStatus, str]] = ..., useNoviFiatFormat: bool = ..., primaryAmount: _Optional[_Union[Money, _Mapping]] = ..., exchangeAmount: _Optional[_Union[Money, _Mapping]] = ...) -> None: ...

class NotificationMessageInfo(_message.Message):
    __slots__ = ["key", "message", "messageTimestamp", "participant"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGETIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    key: MessageKey
    message: Message
    messageTimestamp: int
    participant: str
    def __init__(self, key: _Optional[_Union[MessageKey, _Mapping]] = ..., message: _Optional[_Union[Message, _Mapping]] = ..., messageTimestamp: _Optional[int] = ..., participant: _Optional[str] = ...) -> None: ...

class MediaData(_message.Message):
    __slots__ = ["localPath"]
    LOCALPATH_FIELD_NUMBER: _ClassVar[int]
    localPath: str
    def __init__(self, localPath: _Optional[str] = ...) -> None: ...

class KeepInChat(_message.Message):
    __slots__ = ["keepType", "serverTimestamp", "key", "deviceJid", "clientTimestampMs", "serverTimestampMs"]
    KEEPTYPE_FIELD_NUMBER: _ClassVar[int]
    SERVERTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    DEVICEJID_FIELD_NUMBER: _ClassVar[int]
    CLIENTTIMESTAMPMS_FIELD_NUMBER: _ClassVar[int]
    SERVERTIMESTAMPMS_FIELD_NUMBER: _ClassVar[int]
    keepType: KeepType
    serverTimestamp: int
    key: MessageKey
    deviceJid: str
    clientTimestampMs: int
    serverTimestampMs: int
    def __init__(self, keepType: _Optional[_Union[KeepType, str]] = ..., serverTimestamp: _Optional[int] = ..., key: _Optional[_Union[MessageKey, _Mapping]] = ..., deviceJid: _Optional[str] = ..., clientTimestampMs: _Optional[int] = ..., serverTimestampMs: _Optional[int] = ...) -> None: ...

class NoiseCertificate(_message.Message):
    __slots__ = ["details", "signature"]
    class Details(_message.Message):
        __slots__ = ["serial", "issuer", "expires", "subject", "key"]
        SERIAL_FIELD_NUMBER: _ClassVar[int]
        ISSUER_FIELD_NUMBER: _ClassVar[int]
        EXPIRES_FIELD_NUMBER: _ClassVar[int]
        SUBJECT_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        serial: int
        issuer: str
        expires: int
        subject: str
        key: bytes
        def __init__(self, serial: _Optional[int] = ..., issuer: _Optional[str] = ..., expires: _Optional[int] = ..., subject: _Optional[str] = ..., key: _Optional[bytes] = ...) -> None: ...
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    details: bytes
    signature: bytes
    def __init__(self, details: _Optional[bytes] = ..., signature: _Optional[bytes] = ...) -> None: ...

class CertChain(_message.Message):
    __slots__ = ["leaf", "intermediate"]
    class NoiseCertificate(_message.Message):
        __slots__ = ["details", "signature"]
        class Details(_message.Message):
            __slots__ = ["serial", "issuerSerial", "key", "notBefore", "notAfter"]
            SERIAL_FIELD_NUMBER: _ClassVar[int]
            ISSUERSERIAL_FIELD_NUMBER: _ClassVar[int]
            KEY_FIELD_NUMBER: _ClassVar[int]
            NOTBEFORE_FIELD_NUMBER: _ClassVar[int]
            NOTAFTER_FIELD_NUMBER: _ClassVar[int]
            serial: int
            issuerSerial: int
            key: bytes
            notBefore: int
            notAfter: int
            def __init__(self, serial: _Optional[int] = ..., issuerSerial: _Optional[int] = ..., key: _Optional[bytes] = ..., notBefore: _Optional[int] = ..., notAfter: _Optional[int] = ...) -> None: ...
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        details: bytes
        signature: bytes
        def __init__(self, details: _Optional[bytes] = ..., signature: _Optional[bytes] = ...) -> None: ...
    LEAF_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIATE_FIELD_NUMBER: _ClassVar[int]
    leaf: CertChain.NoiseCertificate
    intermediate: CertChain.NoiseCertificate
    def __init__(self, leaf: _Optional[_Union[CertChain.NoiseCertificate, _Mapping]] = ..., intermediate: _Optional[_Union[CertChain.NoiseCertificate, _Mapping]] = ...) -> None: ...
