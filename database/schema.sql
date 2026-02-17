CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL, 
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
CREATE TABLE books (
	id INTEGER NOT NULL, 
	testament VARCHAR NOT NULL, 
	name VARCHAR NOT NULL, 
	abbreviation VARCHAR NOT NULL, 
	"totalChapters" INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE canons (
	id INTEGER NOT NULL, 
	name VARCHAR NOT NULL, 
	tradition VARCHAR NOT NULL, 
	"totalBooks" INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE book_canon (
	id INTEGER NOT NULL, 
	"canonId" INTEGER NOT NULL, 
	"bookId" INTEGER NOT NULL, 
	"sortIndex" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("bookId") REFERENCES books (id), 
	FOREIGN KEY("canonId") REFERENCES canons (id)
);
CREATE TABLE translations (
	id INTEGER NOT NULL, 
	"canonId" INTEGER NOT NULL, 
	name VARCHAR NOT NULL, 
	description VARCHAR NOT NULL, 
	abbreviation VARCHAR NOT NULL, 
	language VARCHAR NOT NULL, 
	country VARCHAR NOT NULL, 
	"totalVerses" INTEGER NOT NULL, 
	hash VARCHAR NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("canonId") REFERENCES canons (id)
);
CREATE TABLE verses (
	id INTEGER NOT NULL, 
	"translationId" INTEGER NOT NULL, 
	"bookId" INTEGER NOT NULL, 
	chapter INTEGER NOT NULL, 
	"verseNumber" INTEGER NOT NULL, 
	content VARCHAR NOT NULL, title VARCHAR, "saidJesus" INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("bookId") REFERENCES books (id), 
	FOREIGN KEY("translationId") REFERENCES translations (id)
);
CREATE INDEX "ix_verses_bookId" ON verses ("bookId");
CREATE INDEX "ix_verses_translationId" ON verses ("translationId");
CREATE INDEX "ix_verses_translationId_bookId_chapter_verseNumber" ON verses ("translationId", "bookId", chapter, "verseNumber");
CREATE INDEX "ix_translations_canonId" ON translations ("canonId");
